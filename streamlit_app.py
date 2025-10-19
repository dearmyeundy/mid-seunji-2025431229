import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="옴의 법칙 & 회로 시뮬레이터", layout="wide")

st.title("⚡ 옴의 법칙 & 전기 회로 시뮬레이터")
st.write(
    "전압(V), 저항(R)을 조절하여 전류(I)를 관찰하고, 직렬/병렬 회로의 차이를 시각적으로 학습합니다. "
    "슬라이더로 값을 바꾸면 결과가 실시간으로 갱신됩니다."
)

# --- Controls ---
with st.sidebar:
    st.header("입력 (학습용)")
    V = st.slider("전압 V (볼트)", min_value=0.0, max_value=24.0, value=12.0, step=0.1)
    conn = st.radio("회로 연결 방식", ("직렬", "병렬"))
    n_res = st.selectbox("저항 개수", (1, 2, 3))
    Rs = []
    for i in range(n_res):
        Rs.append(st.slider(f"R{i+1} (옴)", min_value=0.1, max_value=1000.0, value=10.0 * (i + 1), step=0.1))

    st.markdown("---")
    if "frame" not in st.session_state:
        st.session_state.frame = 0
    step = st.button("프레임 +1")
    reset = st.button("프레임 초기화")
    animate = st.checkbox("짧은 애니메이션 재생 (학습용)")

if step:
    st.session_state.frame += 1
if reset:
    st.session_state.frame = 0

# --- Physics ---
def total_resistance(resistors, mode):
    if mode == "직렬":
        return sum(resistors)
    else:  # 병렬
        inv = sum((1.0 / r) for r in resistors if r > 0)
        return 1.0 / inv if inv > 0 else 1e-12

R_total = total_resistance(Rs, conn)
if R_total < 1e-9:
    I = float("inf")
else:
    I = V / R_total

# --- Outputs ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("계산 결과")
    st.write(f"총 저항 R_total: **{R_total:.3f} Ω** ({conn})")
    if np.isinf(I):
        st.write("전류 I: **무한대 (단락)**")
    else:
        st.write(f"전류 I: **{I:.4f} A** (V = {V} V)")
    st.write("저항 목록:", ", ".join(f"{r:.1f} Ω" for r in Rs))

with col2:
    st.subheader("V-I 그래프")
    fig_vi, ax_vi = plt.subplots(figsize=(4, 3))
    Vmax = max(24.0, V)
    Vs = np.linspace(0, Vmax, 200)
    if R_total < 1e-9:
        ax_vi.axvline(0, color="gray")
        ax_vi.text(0.5, 0.5, "단락(무한 전류)", transform=ax_vi.transAxes, ha="center")
    else:
        ax_vi.plot(Vs, Vs / R_total, color="tab:blue", lw=2, label=f"I=V/{R_total:.3f}")
        ax_vi.scatter([V], [0 if np.isinf(I) else I], color="red", zorder=5)
        ax_vi.set_xlabel("V (V)")
        ax_vi.set_ylabel("I (A)")
        ax_vi.set_xlim(0, Vmax)
        ax_vi.set_ylim(0, max(0.1, (Vmax / max(R_total, 1e-6)) * 1.2))
        ax_vi.grid(alpha=0.3)
        ax_vi.legend()
    st.pyplot(fig_vi)

# --- Circuit visualizer with moving charges ---
st.subheader("회로 시각화 (전하 흐름)")

def draw_circuit(resistors, mode, current, frame):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

    # loop path coordinates (clockwise)
    path = []
    # left vertical
    path.append(((1, 0.5), (1, 2.5)))
    # top horizontal
    path.append(((1, 2.5), (9, 2.5)))
    # right vertical
    path.append(((9, 2.5), (9, 0.5)))
    # bottom horizontal
    path.append(((9, 0.5), (1, 0.5)))

    # Draw wires
    for seg in path:
        (x1, y1), (x2, y2) = seg
        ax.plot([x1, x2], [y1, y2], color="black", lw=6, solid_capstyle="round", zorder=1)

    # Place resistors on the top segment spaced evenly
    top_xs = np.linspace(2, 8, len(resistors)+2)[1:-1] if len(resistors) > 0 else []
    for i, R in enumerate(resistors):
        cx = top_xs[i]
        cy = 2.5
        # Visual: higher R -> narrower & redder, lower R -> thicker & bluer
        norm = np.clip((R - 0.1) / 100.0, 0, 1)
        color = (1.0, 1.0 - norm, 1.0 - norm)
        linewidth = 12 * (1.0 - 0.8 * norm)  # larger R -> thinner
        ax.plot([cx - 0.4, cx + 0.4], [cy, cy], color=color, lw=linewidth, solid_capstyle="butt", zorder=3)
        ax.text(cx, cy - 0.25, f"R{i+1}={R:.1f}Ω", ha="center", fontsize=8)

    # moving charges along path: speed scaled by current
    # define piecewise path length
    segments = []
    total_len = 0.0
    for (x1, y1), (x2, y2) in path:
        seg_len = np.hypot(x2 - x1, y2 - y1)
        segments.append(((x1, y1, x2, y2), seg_len))
        total_len += seg_len

    # speed factor (pixels per frame) proportional to current (clipped)
    speed = 0.05 + 0.5 * min(10.0, 0 if np.isinf(current) else current)
    # number of charges depends on current magnitude
    n_charges = int(np.clip((0 if np.isinf(current) else current) * 6, 3, 20))
    charges = []
    for k in range(n_charges):
        # phase offset so charges are spaced
        phase = (frame * speed + k * (total_len / n_charges)) % total_len
        # find segment
        acc = 0
        for (x1, y1, x2, y2), seg_len in segments:
            if phase <= acc + seg_len:
                t = (phase - acc) / seg_len
                x = x1 + (x2 - x1) * t
                y = y1 + (y2 - y1) * t
                charges.append((x, y))
                break
            acc += seg_len

    xs = [c[0] for c in charges]
    ys = [c[1] for c in charges]
    ax.scatter(xs, ys, s=40, c="gold", edgecolors="orangered", zorder=4)

    ax.set_title(f"연결: {mode} | I = {'∞' if np.isinf(current) else f'{current:.3f} A'}")
    return fig

# handle short animation: run a few frames if animate checked
placeholder = st.empty()
if animate:
    # play short sequence (non-blocking UI for short time)
    for _ in range(20):
        st.session_state.frame += 1
        fig = draw_circuit(Rs, conn, I, st.session_state.frame)
        placeholder.pyplot(fig)
        time.sleep(0.06)
else:
    fig = draw_circuit(Rs, conn, I, st.session_state.frame)
    placeholder.pyplot(fig)

st.markdown(
    """
학습 포인트:
- V = I × R (옴의 법칙): 고정된 V에서 R이 커지면 I는 작아진다.
- 직렬: R_total = R1 + R2 + ...
- 병렬: 1/R_total = 1/R1 + 1/R2 + ...
\n\n
슬라이더와 저항 색/두께 변화를 관찰하며 전류와 흐름(점의 속도/개수)의 변화를 비교해 보세요.
"""
)

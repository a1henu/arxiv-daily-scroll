---
layout: default
title: Robustness Is a Function, Not a Number: A Factorized Comprehensive Study of OOD Robustness in Vision-Based Driving
---

# Robustness Is a Function, Not a Number: A Factorized Comprehensive Study of OOD Robustness in Vision-Based Driving
**arXiv**：[2602.09018v1](https://arxiv.org/abs/2602.09018) · [PDF](https://arxiv.org/pdf/2602.09018.pdf)  
**作者**：Amir Mallak, Alaa Maalouf  

**一句话要点**：提出因子化方法研究自动驾驶视觉策略的OOD鲁棒性，揭示性能下降的关键因素与设计规则。

**关键词**：自动驾驶鲁棒性, 视觉Transformer策略, 因子化OOD分析, 闭环控制评估, 基础模型特征, 多环境训练

## 3 点简述
- 核心问题：自动驾驶中OOD鲁棒性常被简化为单一数值，掩盖策略失效的具体原因。
- 方法要点：沿场景、季节、天气、时间、智能体混合五轴分解环境，使用VISTA闭环控制评估FC、CNN、ViT策略及FM特征。
- 实验或效果：ViT策略比CNN/FC更鲁棒，FM特征在延迟代价下实现最优性能，多因子交互非加性，训练数据扩展与针对性暴露提升鲁棒性。

## 摘要（原文）

> Out of distribution (OOD) robustness in autonomous driving is often reduced to a single number, hiding what breaks a policy. We decompose environments along five axes: scene (rural/urban), season, weather, time (day/night), and agent mix; and measure performance under controlled $k$-factor perturbations ($k \in \{0,1,2,3\}$). Using closed loop control in VISTA, we benchmark FC, CNN, and ViT policies, train compact ViT heads on frozen foundation-model (FM) features, and vary ID support in scale, diversity, and temporal context. (1) ViT policies are markedly more OOD-robust than comparably sized CNN/FC, and FM features yield state-of-the-art success at a latency cost. (2) Naive temporal inputs (multi-frame) do not beat the best single-frame baseline. (3) The largest single factor drops are rural $\rightarrow$ urban and day $\rightarrow$ night ($\sim 31\%$ each); actor swaps $\sim 10\%$, moderate rain $\sim 7\%$; season shifts can be drastic, and combining a time flip with other changes further degrades performance. (4) FM-feature policies stay above $85\%$ under three simultaneous changes; non-FM single-frame policies take a large first-shift hit, and all no-FM models fall below $50\%$ by three changes. (5) Interactions are non-additive: some pairings partially offset, whereas season-time combinations are especially harmful. (6) Training on winter/snow is most robust to single-factor shifts, while a rural+summer baseline gives the best overall OOD performance. (7) Scaling traces/views improves robustness ($+11.8$ points from $5$ to $14$ traces), yet targeted exposure to hard conditions can substitute for scale. (8) Using multiple ID environments broadens coverage and strengthens weak cases (urban OOD $60.6\% \rightarrow 70.1\%$) with a small ID drop; single-ID preserves peak performance but in a narrow domain. These results yield actionable design rules for OOD-robust driving policies.


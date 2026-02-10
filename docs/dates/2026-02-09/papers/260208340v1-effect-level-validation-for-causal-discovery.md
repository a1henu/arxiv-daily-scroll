---
layout: default
title: Effect-Level Validation for Causal Discovery
---

# Effect-Level Validation for Causal Discovery
**arXiv**：[2602.08340v1](https://arxiv.org/abs/2602.08340) · [PDF](https://arxiv.org/pdf/2602.08340.pdf)  
**作者**：Hoang Dang, Luan Pham, Minh Nguyen  

**一句话要点**：提出效应中心、可容许性优先框架，以提升因果发现在强自选择反馈系统中的决策可靠性

**关键词**：因果发现, 效应验证, 可识别性, 遥测数据, 决策支持, 自选择偏差

## 3 点简述
- 核心问题：因果发现在强自选择反馈系统中，仅依赖图恢复准确性不足以支持可靠决策
- 方法要点：将发现图视为结构假设，通过可识别性、稳定性和证伪性进行评估
- 实验或效果：在真实游戏遥测数据中，发现可识别性是关键瓶颈，部分方法在效应估计上收敛且通过反驳测试

## 摘要（原文）

> Causal discovery is increasingly applied to large-scale telemetry data to estimate the effects of user-facing interventions, yet its reliability for decision-making in feedback-driven systems with strong self-selection remains unclear. In this paper, we propose an effect-centric, admissibility-first framework that treats discovered graphs as structural hypotheses and evaluates them by identifiability, stability, and falsification rather than by graph recovery accuracy alone. Empirically, we study the effect of early exposure to competitive gameplay on short-term retention using real-world game telemetry. We find that many statistically plausible discovery outputs do not admit point-identified causal queries once minimal temporal and semantic constraints are enforced, highlighting identifiability as a critical bottleneck for decision support. When identification is possible, several algorithm families converge to similar, decision-consistent effect estimates despite producing substantially different graph structures, including cases where the direct treatment-outcome edge is absent and the effect is preserved through indirect causal pathways. These converging estimates survive placebo, subsampling, and sensitivity refutation. In contrast, other methods exhibit sporadic admissibility and threshold-sensitive or attenuated effects due to endpoint ambiguity. These results suggest that graph-level metrics alone are inadequate proxies for causal reliability for a given target query. Therefore, trustworthy causal conclusions in telemetry-driven systems require prioritizing admissibility and effect-level validation over causal structural recovery alone.


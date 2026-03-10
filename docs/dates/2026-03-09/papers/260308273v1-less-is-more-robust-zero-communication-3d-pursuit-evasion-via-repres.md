---
layout: default
title: Less is More: Robust Zero-Communication 3D Pursuit-Evasion via Representational Parsimony
---

# Less is More: Robust Zero-Communication 3D Pursuit-Evasion via Representational Parsimony
**arXiv**：[2603.08273v1](https://arxiv.org/abs/2603.08273) · [PDF](https://arxiv.org/pdf/2603.08273.pdf)  
**作者**：Jialin Ying, Zhihao Li, Zicheng Dong, Guohua Wu, Yihuan Liao  

**一句话要点**：提出简约表示与贡献门控信用分配以提升无通信三维追逃的鲁棒性

**关键词**：三维追逃, 无通信协调, 简约表示, 信用分配, 鲁棒性, 多智能体强化学习

## 3 点简述
- 核心问题：非对称三维追逃在通信延迟、部分可观测和非完整机动限制下难以协调
- 方法要点：采用简约演员观察接口和贡献门控信用分配，减少跨智能体耦合
- 实验或效果：在Stage-5评估中成功率提升，并在压力测试和零样本迁移中表现稳健

## 摘要（原文）

> Asymmetric 3D pursuit-evasion in cluttered voxel environments is difficult under communication latency, partial observability, and nonholonomic maneuver limits. While many MARL methods rely on richer inter-agent coupling or centralized signals, these dependencies can become fragility sources when communication is delayed or noisy. Building on an inherited path-guided decentralized pursuit scaffold, we study a robustness-oriented question: can representational parsimony improve communication-free coordination? We instantiate this principle with (i) a parsimonious actor observation interface that removes team-coupled channels (83-D to 50-D), and (ii) Contribution-Gated Credit Assignment (CGCA), a locality-aware credit structure for communication-denied cooperation. In Stage-5 evaluation (4 pursuers vs. 1 evader), our configuration reaches 0.753 +/- 0.091 success and 0.223 +/- 0.066 collision, outperforming the 83-D FULL OBS counterpart (0.721 +/- 0.071, 0.253 +/- 0.089). It further shows graceful degradation under speed/yaw/noise/delay stress tests and resilient zero-shot transfer on urban-canyon maps (about 61% success at density 0.24). These results support a practical paradigm shift: explicitly severing redundant cross-agent channels can suppress compounding error cascades and improve robustness in latency-prone deployment.


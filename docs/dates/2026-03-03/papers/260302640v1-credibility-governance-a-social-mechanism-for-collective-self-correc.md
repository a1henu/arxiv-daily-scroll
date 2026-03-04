---
layout: default
title: Credibility Governance: A Social Mechanism for Collective Self-Correction under Weak Truth Signals
---

# Credibility Governance: A Social Mechanism for Collective Self-Correction under Weak Truth Signals
**arXiv**：[2603.02640v1](https://arxiv.org/abs/2603.02640) · [PDF](https://arxiv.org/pdf/2603.02640.pdf)  
**作者**：Wanying He, Yanxi Lin, Ziheng Zhou, Xue Feng, Min Peng, Qianqian Xie, Zilong Zheng, Yipeng Kang  

**一句话要点**：提出可信度治理机制，以在弱真相信号下提升在线平台集体判断的稳健性。

**关键词**：可信度治理, 集体判断, 意见聚合, 社会模拟, 稳健性评估, 在线平台

## 3 点简述
- 在线平台依赖意见聚合分配资源，但常见信号易放大且不可靠，导致集体判断脆弱。
- 可信度治理通过动态学习代理和观点对公共证据的追踪能力，重新分配影响力。
- 在模拟环境中，该机制优于基线方法，能更快恢复真相状态并增强对抗性压力下的稳健性。

## 摘要（原文）

> Online platforms increasingly rely on opinion aggregation to allocate real-world attention and resources, yet common signals such as engagement votes or capital-weighted commitments are easy to amplify and often track visibility rather than reliability. This makes collective judgments brittle under weak truth signals, noisy or delayed feedback, early popularity surges, and strategic manipulation. We propose Credibility Governance (CG), a mechanism that reallocates influence by learning which agents and viewpoints consistently track evolving public evidence. CG maintains dynamic credibility scores for both agents and opinions, updates opinion influence via credibility-weighted endorsements, and updates agent credibility based on the long-run performance of the opinions they support, rewarding early and persistent alignment with emerging evidence while filtering short-lived noise. We evaluate CG in POLIS, a socio-physical simulation environment that models coupled belief dynamics and downstream feedback under uncertainty. Across settings with initial majority misalignment, observation noise and contamination, and misinformation shocks, CG outperforms vote-based, stake-weighted, and no-governance baselines, yielding faster recovery to the true state, reduced lock-in and path dependence, and improved robustness under adversarial pressure. Our implementation and experimental scripts are publicly available at https://github.com/Wanying-He/Credibility_Governance.


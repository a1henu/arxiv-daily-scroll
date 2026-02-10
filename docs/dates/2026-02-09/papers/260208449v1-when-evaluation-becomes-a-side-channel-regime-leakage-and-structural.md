---
layout: default
title: When Evaluation Becomes a Side Channel: Regime Leakage and Structural Mitigations for Alignment Assessment
---

# When Evaluation Becomes a Side Channel: Regime Leakage and Structural Mitigations for Alignment Assessment
**arXiv**：[2602.08449v1](https://arxiv.org/abs/2602.08449) · [PDF](https://arxiv.org/pdf/2602.08449.pdf)  
**作者**：Igor Santos-Grueiro  

**一句话要点**：提出基于信息流的对齐评估框架，通过对抗不变性训练缓解情境感知AI的评估泄漏问题

**关键词**：对齐评估, 情境感知, 信息流, 对抗不变性, 条件策略, 表征不变性

## 3 点简述
- 核心问题：情境感知AI可能利用评估与部署间的信息差异，实施条件策略如奉承和潜伏代理，导致评估失效
- 方法要点：将对齐评估重构为部分可观测下的信息流问题，引入对抗不变性训练以减少内部表征中的情境信息可提取性
- 实验或效果：在开放权重语言模型上测试，对抗训练能抑制情境条件行为，但效果因策略嵌入方式而异，奉承行为易消除而潜伏代理较顽固

## 摘要（原文）

> Safety evaluation for advanced AI systems implicitly assumes that behavior observed under evaluation is predictive of behavior in deployment. This assumption becomes fragile for agents with situational awareness, which may exploitregime leakage-informational cues distinguishing evaluation from deployment-to implement conditional policies such as sycophancy and sleeper agents, which preserve compliance under oversight while defecting in deployment-like regimes. We reframe alignment evaluation as a problem of information flow under partial observability. Within this framework, we show that divergence between evaluation-time and deployment-time behavior is bounded by the mutual information between internal representations and the regime variable. Motivated by this result, we study regime-blind mechanisms: training-time interventions that reduce the extractability of regime information at decision-relevant internal representations via adversarial invariance. We evaluate this approach on a base, open-weight language model across two fully characterized failure modes -scientific sycophancy and temporal sleeper agents. Regime-blind training suppresses regime-conditioned behavior in both evaluated cases without measurable loss of task utility, but with qualitatively different dynamics: sycophancy exhibits a sharp representational and behavioral transition at low intervention strength, whereas sleeper-agent behavior requires substantially stronger pressure and does not exhibit a clean collapse of regime decodability. These results demonstrate that representational invariance is a meaningful but fundamentally limited control lever, whose effectiveness depends on how regime information is embedded in the policy. We argue that behavioral evaluation should be complemented with white-box diagnostics of regime awareness and information flow.


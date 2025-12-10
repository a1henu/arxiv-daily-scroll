---
layout: default
title: Information-Dense Reasoning for Efficient and Auditable Security Alert Triage
---

# Information-Dense Reasoning for Efficient and Auditable Security Alert Triage
**arXiv**：[2512.08169v1](https://arxiv.org/abs/2512.08169) · [PDF](https://arxiv.org/pdf/2512.08169.pdf)  
**作者**：Guangze Zhao, Yongzheng Zhang, Changbo Tian, Dan Xie, Hongri Liu, Bailing Wang  

**一句话要点**：提出AIDR混合云边框架，通过信息密度优化解决安全告警分诊中的延迟与可审计性矛盾

**关键词**：安全告警分诊, 信息密度优化, 推理链压缩, 云边计算, 可审计性, 延迟优化

## 3 点简述
- 核心问题：安全运营中心面临告警分诊延迟悖论——详尽推理链确保准确性但延迟高，精简链则牺牲可审计性
- 方法要点：采用梯度压缩技术精简推理链，保留决策关键步骤，构建云边架构实现高效路由与本地处理
- 实验效果：相比思维链方法，AIDR实现更高准确率与40.6%延迟降低，保持数据驻留合规性

## 摘要（原文）

> Security Operations Centers face massive, heterogeneous alert streams under minute-level service windows, creating the Alert Triage Latency Paradox: verbose reasoning chains ensure accuracy and compliance but incur prohibitive latency and token costs, while minimal chains sacrifice transparency and auditability. Existing solutions fail: signature systems are brittle, anomaly methods lack actionability, and fully cloud-hosted LLMs raise latency, cost, and privacy concerns. We propose AIDR, a hybrid cloud-edge framework that addresses this trade-off through constrained information-density optimization. The core innovation is gradient-based compression of reasoning chains to retain only decision-critical steps--minimal evidence sufficient to justify predictions while respecting token and latency budgets. We demonstrate that this approach preserves decision-relevant information while minimizing complexity. We construct compact datasets by distilling alerts into 3-5 high-information bullets (68% token reduction), train domain-specialized experts via LoRA, and deploy a cloud-edge architecture: a cloud LLM routes alerts to on-premises experts generating SOAR-ready JSON. Experiments demonstrate AIDR achieves higher accuracy and 40.6% latency reduction versus Chain-of-Thought, with robustness to data corruption and out-of-distribution generalization, enabling auditable and efficient SOC triage with full data residency compliance.


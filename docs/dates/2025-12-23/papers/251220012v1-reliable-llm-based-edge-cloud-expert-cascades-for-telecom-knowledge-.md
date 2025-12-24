---
layout: default
title: Reliable LLM-Based Edge-Cloud-Expert Cascades for Telecom Knowledge Systems
---

# Reliable LLM-Based Edge-Cloud-Expert Cascades for Telecom Knowledge Systems
**arXiv**：[2512.20012v1](https://arxiv.org/abs/2512.20012) · [PDF](https://arxiv.org/pdf/2512.20012.pdf)  
**作者**：Qiushuo Hou, Sangwoo Park, Matteo Zecchin, Yunlong Cai, Guanding Yu, Osvaldo Simeone, Tommaso Melodia  

**一句话要点**：提出基于边缘-云-专家级联的LLM知识系统，以优化电信领域问答的成本与可靠性。

**关键词**：级联LLM系统, 电信知识问答, 多假设检验, 成本优化, 可靠性保证

## 3 点简述
- 核心问题：LLM在电信自动化部署中需平衡推理成本、延迟和可靠性。
- 方法要点：通过多假设检验选择阈值，构建级联系统，确保答案与专家判断对齐。
- 实验或效果：在TeleQnA数据集上验证，相比基线方法，在保证可靠性下实现更优成本效率。

## 摘要（原文）

> Large language models (LLMs) are emerging as key enablers of automation in domains such as telecommunications, assisting with tasks including troubleshooting, standards interpretation, and network optimization. However, their deployment in practice must balance inference cost, latency, and reliability. In this work, we study an edge-cloud-expert cascaded LLM-based knowledge system that supports decision-making through a question-and-answer pipeline. In it, an efficient edge model handles routine queries, a more capable cloud model addresses complex cases, and human experts are involved only when necessary. We define a misalignment-cost constrained optimization problem, aiming to minimize average processing cost, while guaranteeing alignment of automated answers with expert judgments. We propose a statistically rigorous threshold selection method based on multiple hypothesis testing (MHT) for a query processing mechanism based on knowledge and confidence tests. The approach provides finite-sample guarantees on misalignment risk. Experiments on the TeleQnA dataset -- a telecom-specific benchmark -- demonstrate that the proposed method achieves superior cost-efficiency compared to conventional cascaded baselines, while ensuring reliability at prescribed confidence levels.


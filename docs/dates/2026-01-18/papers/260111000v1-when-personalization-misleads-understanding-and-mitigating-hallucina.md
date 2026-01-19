---
layout: default
title: When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs
---

# When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs
**arXiv**：[2601.11000v1](https://arxiv.org/abs/2601.11000) · [PDF](https://arxiv.org/pdf/2601.11000.pdf)  
**作者**：Zhongxiang Sun, Yi Zhan, Chenglei Shen, Weijie Yu, Xiao Zhang, Ming He, Jun Xu  

**一句话要点**：提出Factuality-Preserving Personalized Steering以缓解个性化大语言模型中的幻觉问题

**关键词**：个性化大语言模型, 幻觉缓解, 事实保持, 推理时方法, 基准评估

## 3 点简述
- 个性化大语言模型在事实查询中可能因用户历史偏好而产生幻觉，降低事实可靠性
- 提出FPPS方法，在推理时轻量级地缓解事实扭曲，同时保持个性化行为
- 实验表明FPPS在多模型上显著提升事实准确性，并引入PFQABench基准进行评估

## 摘要（原文）

> Personalized large language models (LLMs) adapt model behavior to individual users to enhance user satisfaction, yet personalization can inadvertently distort factual reasoning. We show that when personalized LLMs face factual queries, there exists a phenomenon where the model generates answers aligned with a user's prior history rather than the objective truth, resulting in personalization-induced hallucinations that degrade factual reliability and may propagate incorrect beliefs, due to representational entanglement between personalization and factual representations. To address this issue, we propose Factuality-Preserving Personalized Steering (FPPS), a lightweight inference-time approach that mitigates personalization-induced factual distortions while preserving personalized behavior. We further introduce PFQABench, the first benchmark designed to jointly evaluate factual and personalized question answering under personalization. Experiments across multiple LLM backbones and personalization methods show that FPPS substantially improves factual accuracy while maintaining personalized performance.


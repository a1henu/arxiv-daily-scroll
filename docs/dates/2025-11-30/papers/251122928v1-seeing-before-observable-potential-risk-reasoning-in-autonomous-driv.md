---
layout: default
title: Seeing before Observable: Potential Risk Reasoning in Autonomous Driving via Vision Language Models
---

# Seeing before Observable: Potential Risk Reasoning in Autonomous Driving via Vision Language Models
**arXiv**：[2511.22928v1](https://arxiv.org/abs/2511.22928) · [PDF](https://arxiv.org/pdf/2511.22928.pdf)  
**作者**：Jiaxin Liu, Xiangyu Yan, Liang Peng, Lei Yang, Lingjun Zhang, Yuechen Luo, Yueming Tao, Ashton Yu Xuan Tan, Mu Li, Lei Zhang, Ziqi Zhan, Sai Guo, Hong Wang, Jun Li  

**一句话要点**：提出PotentialRiskQA数据集和PR-Reasoner框架，以解决自动驾驶中潜在风险推理问题。

**关键词**：自动驾驶安全, 潜在风险推理, 视觉语言模型, 数据集构建, 语义理解

## 3 点简述
- 核心问题：自动驾驶在罕见复杂场景中，难以识别未观察到的潜在风险，如基于细微前兆的推理。
- 方法要点：构建PotentialRiskQA视觉语言数据集，包含结构化场景描述、语义前兆和风险结果标注。
- 实验或效果：基于数据集微调PR-Reasoner，相比基线视觉语言模型，显著提升潜在风险推理性能。

## 摘要（原文）

> Ensuring safety remains a key challenge for autonomous vehicles (AVs), especially in rare and complex scenarios. One critical but understudied aspect is the \textbf{potential risk} situations, where the risk is \textbf{not yet observable} but can be inferred from subtle precursors, such as anomalous behaviors or commonsense violations. Recognizing these precursors requires strong semantic understanding and reasoning capabilities, which are often absent in current AV systems due to the scarcity of such cases in existing driving or risk-centric datasets. Moreover, current autonomous driving accident datasets often lack annotations of the causal reasoning chains behind incidents, which are essential for identifying potential risks before they become observable. To address these gaps, we introduce PotentialRiskQA, a novel vision-language dataset designed for reasoning about potential risks prior to observation. Each sample is annotated with structured scene descriptions, semantic precursors, and inferred risk outcomes. Based on this dataset, we further propose PR-Reasoner, a vision-language-model-based framework tailored for onboard potential risk reasoning. Experimental results show that fine-tuning on PotentialRiskQA enables PR-Reasoner to significantly enhance its performance on the potential risk reasoning task compared to baseline VLMs. Together, our dataset and model provide a foundation for developing autonomous systems with improved foresight and proactive safety capabilities, moving toward more intelligent and resilient AVs.


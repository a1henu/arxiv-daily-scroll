---
layout: default
title: From Data to Behavior: Predicting Unintended Model Behaviors Before Training
---

# From Data to Behavior: Predicting Unintended Model Behaviors Before Training
**arXiv**：[2602.04735v1](https://arxiv.org/abs/2602.04735) · [PDF](https://arxiv.org/pdf/2602.04735.pdf)  
**作者**：Mengru Wang, Zhenqian Xu, Junfeng Fang, Yunzhi Yao, Shumin Deng, Huajun Chen, Ningyu Zhang  

**一句话要点**：提出Data2Behavior任务和MDF方法，以在训练前预测大语言模型的无意行为，降低微调成本。

**关键词**：大语言模型, 无意行为预测, 数据特征操纵, 安全风险评估, 预训练漏洞分析

## 3 点简述
- 核心问题：大语言模型可能从良性数据中习得无意偏见，现有方法难以在微调前检测风险。
- 方法要点：MDF通过数据均值表示注入基础模型前向传播，无需参数更新，揭示潜在偏见和安全风险。
- 实验或效果：在多个模型上验证MDF能可靠预测无意行为，GPU资源消耗仅为微调的约20%。

## 摘要（原文）

> Large Language Models (LLMs) can acquire unintended biases from seemingly benign training data even without explicit cues or malicious content. Existing methods struggle to detect such risks before fine-tuning, making post hoc evaluation costly and inefficient. To address this challenge, we introduce Data2Behavior, a new task for predicting unintended model behaviors prior to training. We also propose Manipulating Data Features (MDF), a lightweight approach that summarizes candidate data through their mean representations and injects them into the forward pass of a base model, allowing latent statistical signals in the data to shape model activations and reveal potential biases and safety risks without updating any parameters. MDF achieves reliable prediction while consuming only about 20% of the GPU resources required for fine-tuning. Experiments on Qwen3-14B, Qwen2.5-32B-Instruct, and Gemma-3-12b-it confirm that MDF can anticipate unintended behaviors and provide insight into pre-training vulnerabilities.


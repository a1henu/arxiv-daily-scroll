---
layout: default
title: AttenMIA: LLM Membership Inference Attack through Attention Signals
---

# AttenMIA: LLM Membership Inference Attack through Attention Signals
**arXiv**：[2601.18110v1](https://arxiv.org/abs/2601.18110) · [PDF](https://arxiv.org/pdf/2601.18110.pdf)  
**作者**：Pedram Zaree, Md Abdullah Al Mamun, Yue Dong, Ihsen Alouani, Nael Abu-Ghazaleh  

**一句话要点**：提出AttenMIA，利用Transformer自注意力信号进行LLM成员推断攻击，提升攻击成功率。

**关键词**：成员推断攻击, 自注意力机制, 隐私风险, Transformer模型, 数据提取攻击

## 3 点简述
- 核心问题：LLM训练数据记忆引发隐私风险，现有成员推断攻击依赖输出置信度或嵌入特征，效果有限。
- 方法要点：通过分析Transformer自注意力模式，结合扰动散度指标，训练MIA分类器。
- 实验或效果：在LLaMA-2等模型上实验，注意力特征优于基线，在低误报率下表现突出，并提升数据提取攻击效果。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed to enable or improve a multitude of real-world applications. Given the large size of their training data sets, their tendency to memorize training data raises serious privacy and intellectual property concerns. A key threat is the membership inference attack (MIA), which aims to determine whether a given sample was included in the model's training set. Existing MIAs for LLMs rely primarily on output confidence scores or embedding-based features, but these signals are often brittle, leading to limited attack success. We introduce AttenMIA, a new MIA framework that exploits self-attention patterns inside the transformer model to infer membership. Attention controls the information flow within the transformer, exposing different patterns for memorization that can be used to identify members of the dataset. Our method uses information from attention heads across layers and combines them with perturbation-based divergence metrics to train an effective MIA classifier. Using extensive experiments on open-source models including LLaMA-2, Pythia, and Opt models, we show that attention-based features consistently outperform baselines, particularly under the important low-false-positive metric (e.g., achieving up to 0.996 ROC AUC & 87.9% TPR@1%FPR on the WikiMIA-32 benchmark with Llama2-13b). We show that attention signals generalize across datasets and architectures, and provide a layer- and head-level analysis of where membership leakage is most pronounced. We also show that using AttenMIA to replace other membership inference attacks in a data extraction framework results in training data extraction attacks that outperform the state of the art. Our findings reveal that attention mechanisms, originally introduced to enhance interpretability, can inadvertently amplify privacy risks in LLMs, underscoring the need for new defenses.


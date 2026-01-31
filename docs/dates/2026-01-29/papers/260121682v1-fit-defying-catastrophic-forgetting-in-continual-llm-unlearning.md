---
layout: default
title: FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning
---

# FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning
**arXiv**：[2601.21682v1](https://arxiv.org/abs/2601.21682) · [PDF](https://arxiv.org/pdf/2601.21682.pdf)  
**作者**：Xiaoyu Xu, Minxin Du, Kun Fang, Zi Liang, Yaxin Xiao, Zhicong Huang, Cheng Hong, Qingqing Ye, Haibo Hu  

**一句话要点**：提出FIT框架以解决大语言模型持续遗忘中的灾难性遗忘问题

**关键词**：大语言模型遗忘, 灾难性遗忘, 持续学习, 隐私保护, 模型鲁棒性, 基准测试

## 3 点简述
- 核心问题：现有大语言模型遗忘方法难以处理现实世界中持续、大量的删除请求，导致性能下降和灾难性遗忘。
- 方法要点：FIT通过数据过滤、重要性感知更新和针对性层归因，实现稳定遗忘并平衡遗忘效果与模型效用。
- 实验或效果：在PCH基准测试中，FIT在数百个删除请求下，在多个任务上超越现有方法，并抵抗重新学习和量化恢复攻击。

## 摘要（原文）

> Large language models (LLMs) demonstrate impressive capabilities across diverse tasks but raise concerns about privacy, copyright, and harmful materials. Existing LLM unlearning methods rarely consider the continual and high-volume nature of real-world deletion requests, which can cause utility degradation and catastrophic forgetting as requests accumulate. To address this challenge, we introduce \fit, a framework for continual unlearning that handles large numbers of deletion requests while maintaining robustness against both catastrophic forgetting and post-unlearning recovery. \fit mitigates degradation through rigorous data \underline{F}iltering, \underline{I}mportance-aware updates, and \underline{T}argeted layer attribution, enabling stable performance across long sequences of unlearning operations and achieving a favorable balance between forgetting effectiveness and utility retention. To support realistic evaluation, we present \textbf{PCH}, a benchmark covering \textbf{P}ersonal information, \textbf{C}opyright, and \textbf{H}armful content in sequential deletion scenarios, along with two symmetric metrics, Forget Degree (F.D.) and Retain Utility (R.U.), which jointly assess forgetting quality and utility preservation. Extensive experiments on four open-source LLMs with hundreds of deletion requests show that \fit achieves the strongest trade-off between F.D. and R.U., surpasses existing methods on MMLU, CommonsenseQA, and GSM8K, and remains resistant against both relearning and quantization recovery attacks.


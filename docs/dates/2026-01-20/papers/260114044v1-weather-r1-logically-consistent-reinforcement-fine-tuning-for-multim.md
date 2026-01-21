---
layout: default
title: Weather-R1: Logically Consistent Reinforcement Fine-Tuning for Multimodal Reasoning in Meteorology
---

# Weather-R1: Logically Consistent Reinforcement Fine-Tuning for Multimodal Reasoning in Meteorology
**arXiv**：[2601.14044v1](https://arxiv.org/abs/2601.14044) · [PDF](https://arxiv.org/pdf/2601.14044.pdf)  
**作者**：Kaiyu Wu, Pucheng Han, Hualong Zhang, Naigeng Wu, Keze Wang  

**一句话要点**：提出逻辑一致强化微调方法，解决气象领域多模态推理中的自相矛盾问题。

**关键词**：气象多模态推理, 逻辑一致性强化微调, 自相矛盾推理, WeatherQA基准, 视觉语言模型

## 3 点简述
- 气象领域视觉语言模型存在领域差距和推理忠实性差距，主流强化微调易导致自相矛盾推理。
- 引入逻辑一致性奖励，提出逻辑一致强化微调方法，构建WeatherQA基准。
- Weather-R1模型在WeatherQA上性能提升9.8个百分点，超越基准和原始模型。

## 摘要（原文）

> While Vision Language Models (VLMs) show advancing reasoning capabilities, their application in meteorology is constrained by a domain gap and a reasoning faithfulness gap. Specifically, mainstream Reinforcement Fine-Tuning (RFT) can induce Self-Contradictory Reasoning (Self-Contra), where the model's reasoning contradicts its final answer, which is unacceptable in such a high-stakes domain. To address these challenges, we construct WeatherQA, a novel multimodal reasoning benchmark in meteorology. We also propose Logically Consistent Reinforcement Fine-Tuning (LoCo-RFT), which resolves Self-Contra by introducing a logical consistency reward. Furthermore, we introduce Weather-R1, the first reasoning VLM with logical faithfulness in meteorology, to the best of our knowledge. Experiments demonstrate that Weather-R1 improves performance on WeatherQA by 9.8 percentage points over the baseline, outperforming Supervised Fine-Tuning and RFT, and even surpassing the original Qwen2.5-VL-32B. These results highlight the effectiveness of our LoCo-RFT and the superiority of Weather-R1. Our benchmark and code are available at https://github.com/Marcowky/Weather-R1.


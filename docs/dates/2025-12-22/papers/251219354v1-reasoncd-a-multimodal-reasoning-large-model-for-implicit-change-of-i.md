---
layout: default
title: ReasonCD: A Multimodal Reasoning Large Model for Implicit Change-of-Interest Semantic Mining
---

# ReasonCD: A Multimodal Reasoning Large Model for Implicit Change-of-Interest Semantic Mining
**arXiv**：[2512.19354v1](https://arxiv.org/abs/2512.19354) · [PDF](https://arxiv.org/pdf/2512.19354.pdf)  
**作者**：Zhenyang Huang, Xiao Yu, Yi Zhang, Decheng Wang, Hang Ruan  

**一句话要点**：提出ReasonCD模型以解决遥感变化检测中隐含兴趣变化语义挖掘问题

**关键词**：遥感变化检测, 多模态推理, 隐含语义挖掘, 大语言模型, 兴趣变化区域

## 3 点简述
- 核心问题：现有方法依赖显式文本描述，无法处理隐含兴趣变化语义，导致性能下降。
- 方法要点：利用预训练大语言模型的推理能力挖掘用户隐含任务意图，指导变化检测。
- 实验或效果：在BCDD数据集上F1分数达92.1%，并在推理数据上验证了模型解释能力。

## 摘要（原文）

> Remote sensing image change detection is one of the fundamental tasks in remote sensing intelligent interpretation. Its core objective is to identify changes within change regions of interest (CRoI). Current multimodal large models encode rich human semantic knowledge, which is utilized for guidance in tasks such as remote sensing change detection. However, existing methods that use semantic guidance for detecting users' CRoI overly rely on explicit textual descriptions of CRoI, leading to the problem of near-complete performance failure when presented with implicit CRoI textual descriptions. This paper proposes a multimodal reasoning change detection model named ReasonCD, capable of mining users' implicit task intent. The model leverages the powerful reasoning capabilities of pre-trained large language models to mine users' implicit task intents and subsequently obtains different change detection results based on these intents. Experiments on public datasets demonstrate that the model achieves excellent change detection performance, with an F1 score of 92.1\% on the BCDD dataset. Furthermore, to validate its superior reasoning functionality, this paper annotates a subset of reasoning data based on the SECOND dataset. Experimental results show that the model not only excels at basic reasoning-based change detection tasks but can also explain the reasoning process to aid human decision-making.


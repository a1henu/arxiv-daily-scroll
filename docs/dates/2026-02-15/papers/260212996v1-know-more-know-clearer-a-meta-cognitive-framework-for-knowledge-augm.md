---
layout: default
title: Know More, Know Clearer: A Meta-Cognitive Framework for Knowledge Augmentation in Large Language Models
---

# Know More, Know Clearer: A Meta-Cognitive Framework for Knowledge Augmentation in Large Language Models
**arXiv**：[2602.12996v1](https://arxiv.org/abs/2602.12996) · [PDF](https://arxiv.org/pdf/2602.12996.pdf)  
**作者**：Hao Chen, Ye He, Yuchun Fan, Yukun Yan, Zhenghao Liu, Qingfu Zhu, Maosong Sun, Wanxiang Che  

**一句话要点**：提出元认知框架以解决大语言模型知识增强中的知识-置信度差距问题

**关键词**：知识增强, 元认知框架, 大语言模型, 置信度校准, 认知一致性

## 3 点简述
- 核心问题：现有知识增强方法忽视知识-置信度差距，导致过度自信错误或不确定真相
- 方法要点：利用内部认知信号划分知识空间，并通过认知一致性机制同步主观确定性与客观准确性
- 实验或效果：广泛实验显示框架优于基线，增强知识能力并促进区分已知与未知的认知行为

## 摘要（原文）

> Knowledge augmentation has significantly enhanced the performance of Large Language Models (LLMs) in knowledge-intensive tasks. However, existing methods typically operate on the simplistic premise that model performance equates with internal knowledge, overlooking the knowledge-confidence gaps that lead to overconfident errors or uncertain truths. To bridge this gap, we propose a novel meta-cognitive framework for reliable knowledge augmentation via differentiated intervention and alignment. Our approach leverages internal cognitive signals to partition the knowledge space into mastered, confused, and missing regions, guiding targeted knowledge expansion. Furthermore, we introduce a cognitive consistency mechanism to synchronize subjective certainty with objective accuracy, ensuring calibrated knowledge boundaries. Extensive experiments demonstrate the our framework consistently outperforms strong baselines, validating its rationality in not only enhancing knowledge capabilities but also fostering cognitive behaviors that better distinguish knowns from unknowns.


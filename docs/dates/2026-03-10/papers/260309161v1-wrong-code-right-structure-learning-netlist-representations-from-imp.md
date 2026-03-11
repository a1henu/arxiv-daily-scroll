---
layout: default
title: Wrong Code, Right Structure: Learning Netlist Representations from Imperfect LLM-Generated RTL
---

# Wrong Code, Right Structure: Learning Netlist Representations from Imperfect LLM-Generated RTL
**arXiv**：[2603.09161v1](https://arxiv.org/abs/2603.09161) · [PDF](https://arxiv.org/pdf/2603.09161.pdf)  
**作者**：Siyang Cai, Cangyuan Li, Yinhe Han, Ying Wang  

**一句话要点**：提出利用不完美LLM生成RTL进行网表表示学习的数据增强框架，以解决电路分析中标注数据稀缺问题。

**关键词**：网表表示学习, 数据增强, LLM生成RTL, 电路分析, 功能理解任务

## 3 点简述
- 核心问题：电路网表表示学习受限于标注数据稀缺，因真实设计受知识产权保护且标注成本高。
- 方法要点：利用LLM生成的功能不完美RTL，其合成网表仍保留结构模式，作为训练数据进行成本有效的数据增强。
- 实验或效果：在电路功能理解任务上评估，模型在真实网表上泛化良好，匹配或超越基于稀缺高质量数据的方法。

## 摘要（原文）

> Learning effective netlist representations is fundamentally constrained by the scarcity of labeled datasets, as real designs are protected by Intellectual Property (IP) and costly to annotate. Existing work therefore focuses on small-scale circuits with clean labels, limiting scalability to realistic designs. Meanwhile, Large Language Models (LLMs) can generate Register-Transfer-Level (RTL) at scale, but their functional incorrectness has hindered their use in circuit analysis. In this work, we make a key observation: even when LLM-Generated RTL is functionally imperfect, the synthesized netlists still preserve structural patterns that are strongly indicative of the intended functionality. Building on this insight, we propose a cost-effective data augmentation and training framework that systematically exploits imperfect LLM-Generated RTL as training data for netlist representation learning, forming an end-to-end pipeline from automated code generation to downstream tasks. We conduct evaluations on circuit functional understanding tasks, including sub-circuit boundary identification and component classification, across benchmarks of increasing scales, extending the task scope from operator-level to IP-level. The evaluations demonstrate that models trained on our noisy synthetic corpus generalize well to real-world netlists, matching or even surpassing methods trained on scarce high-quality data and effectively breaking the data bottleneck in circuit representation learning.


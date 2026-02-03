---
layout: default
title: EvoMU: Evolutionary Machine Unlearning
---

# EvoMU: Evolutionary Machine Unlearning
**arXiv**：[2602.02139v1](https://arxiv.org/abs/2602.02139) · [PDF](https://arxiv.org/pdf/2602.02139.pdf)  
**作者**：Pawel Batorski, Paul Swoboda  

**一句话要点**：提出EvoMU通过进化搜索自动发现任务特定损失函数以优化机器遗忘性能

**关键词**：机器遗忘, 进化搜索, 损失函数优化, AI协同科学家, 小模型应用

## 3 点简述
- 机器遗忘需平衡遗忘与保留数据，现有损失函数搜索空间大且缺乏通用最优解
- EvoMU采用进化搜索自动生成数据集特定损失函数，无需人工干预
- 在TOFU-5%等基准上超越先前方法，使用4B参数模型实现SotA结果

## 摘要（原文）

> Machine unlearning aims to unlearn specified training data (e.g. sensitive or copyrighted material). A prominent approach is to fine-tune an existing model with an unlearning loss that retains overall utility. The space of suitable unlearning loss functions is vast, making the search for an optimal loss function daunting. Additionally, there might not even exist a universally optimal loss function: differences in the structure and overlap of the forget and retain data can cause a loss to work well in one setting but over-unlearn or under-unlearn in another. Our approach EvoMU tackles these two challenges simultaneously. An evolutionary search procedure automatically finds task-specific losses in the vast space of possible unlearning loss functions. This allows us to find dataset-specific losses that match or outperform existing losses from the literature, without the need for a human-in-the-loop. This work is therefore an instance of automatic scientific discovery, a.k.a. an AI co-scientist. In contrast to previous AI co-scientist works, we do so on a budget: We achieve SotA results using a small 4B parameter model (Qwen3-4B-Thinking), showing the potential of AI co-scientists with limited computational resources. Our experimental evaluation shows that we surpass previous loss-based unlearning formulations on TOFU-5%, TOFU-10%, MUSE and WMDP by synthesizing novel unlearning losses. Our code is available at https://github.com/Batorskq/EvoMU.


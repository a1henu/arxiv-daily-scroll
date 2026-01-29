---
layout: default
title: IOTA: Corrective Knowledge-Guided Prompt Learning via Black-White Box Framework
---

# IOTA: Corrective Knowledge-Guided Prompt Learning via Black-White Box Framework
**arXiv**：[2601.20526v1](https://arxiv.org/abs/2601.20526) · [PDF](https://arxiv.org/pdf/2601.20526.pdf)  
**作者**：Shaokun Wang, Yifan Yu, Yuhang He, Weili Guan, Yihong Gong  

**一句话要点**：提出IOTA框架，通过黑白盒结合与纠正知识引导，提升预训练模型在下游任务中的适应能力。

**关键词**：参数高效调优, 黑白盒框架, 纠正知识引导, 提示学习, 下游任务适应, 图像分类

## 3 点简述
- 核心问题：现有参数高效调优方法将预训练模型视为黑盒，依赖数据驱动，未充分利用其先验知识，限制下游任务适应潜力。
- 方法要点：IOTA框架整合数据驱动的黑盒模块与知识驱动的白盒模块，白盒模块通过对比错误预测与正确认知生成纠正知识，并转化为可解释提示引导黑盒模块。
- 实验或效果：在12个图像分类基准上，通过少样本和易到难适应设置验证了纠正知识的有效性和方法的优越性。

## 摘要（原文）

> Recently, adapting pre-trained models to downstream tasks has attracted increasing interest. Previous Parameter-Efficient-Tuning (PET) methods regard the pre-trained model as an opaque Black Box model, relying purely on data-driven optimization and underutilizing their inherent prior knowledge. This oversight limits the models' potential for effective downstream task adaptation. To address these issues, we propose a novel black-whIte bOx prompT leArning framework (IOTA), which integrates a data-driven Black Box module with a knowledge-driven White Box module for downstream task adaptation. Specifically, the White Box module derives corrective knowledge by contrasting the wrong predictions with the right cognition. This knowledge is verbalized into interpretable human prompts and leveraged through a corrective knowledge-guided prompt selection strategy to guide the Black Box module toward more accurate predictions. By jointly leveraging knowledge- and data-driven learning signals, IOTA achieves effective downstream task adaptation. Experimental results on 12 image classification benchmarks under few-shot and easy-to-hard adaptation settings demonstrate the effectiveness of corrective knowledge and the superiority of our method over state-of-the-art methods.


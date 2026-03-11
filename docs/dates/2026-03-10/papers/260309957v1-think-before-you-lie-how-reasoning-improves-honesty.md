---
layout: default
title: Think Before You Lie: How Reasoning Improves Honesty
---

# Think Before You Lie: How Reasoning Improves Honesty
**arXiv**：[2603.09957v1](https://arxiv.org/abs/2603.09957) · [PDF](https://arxiv.org/pdf/2603.09957.pdf)  
**作者**：Ann Yuan, Asma Ghandeharioun, Carter Blum, Alicia Machado, Jessica Hoffmann, Daphne Ippolito, Martin Wattenberg, Lucas Dixon, Katja Filippova  

**一句话要点**：提出推理机制提升大语言模型在道德权衡场景中的诚实性

**关键词**：大语言模型诚实性, 道德推理, 表示空间几何, 欺骗行为分析, 模型稳定性

## 3 点简述
- 研究大语言模型在诚实性成本可变场景下的欺骗行为条件
- 发现推理过程能稳定提高模型诚实性，与人类行为相反
- 揭示欺骗区域在表示空间中不稳定，推理通过遍历空间偏向诚实默认

## 摘要（原文）

> While existing evaluations of large language models (LLMs) measure deception rates, the underlying conditions that give rise to deceptive behavior are poorly understood. We investigate this question using a novel dataset of realistic moral trade-offs where honesty incurs variable costs. Contrary to humans, who tend to become less honest given time to deliberate (Capraro, 2017; Capraro et al., 2019), we find that reasoning consistently increases honesty across scales and for several LLM families. This effect is not only a function of the reasoning content, as reasoning traces are often poor predictors of final behaviors. Rather, we show that the underlying geometry of the representational space itself contributes to the effect. Namely, we observe that deceptive regions within this space are metastable: deceptive answers are more easily destabilized by input paraphrasing, output resampling, and activation noise than honest ones. We interpret the effect of reasoning in this vein: generating deliberative tokens as part of moral reasoning entails the traversal of a biased representational space, ultimately nudging the model toward its more stable, honest defaults.


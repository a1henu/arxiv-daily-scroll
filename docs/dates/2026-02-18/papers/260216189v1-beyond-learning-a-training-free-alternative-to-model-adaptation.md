---
layout: default
title: Beyond Learning: A Training-Free Alternative to Model Adaptation
---

# Beyond Learning: A Training-Free Alternative to Model Adaptation
**arXiv**：[2602.16189v1](https://arxiv.org/abs/2602.16189) · [PDF](https://arxiv.org/pdf/2602.16189.pdf)  
**作者**：Namkyung Yoon, Kyeonghyun Yoo, Wooyong Jung, Sanghong Kim, Hwangnam Kim  

**一句话要点**：提出模型移植技术以无需训练实现语言模型功能改进

**关键词**：语言模型, 模型移植, 激活分析, 模块化, 无训练优化, 性能恢复

## 3 点简述
- 核心问题：语言模型有时性能下降，现有方法资源消耗大。
- 方法要点：通过激活分析识别局部模块，移植激活合适的模块至目标模型。
- 实验或效果：移植显著提升性能，在跨代和指令调优实验中恢复率可达100%以上。

## 摘要（原文）

> Despite the continuous research and evolution of language models, they sometimes underperform previous versions. Existing approaches to overcome these challenges are resource-intensive, highlighting the need for alternatives that enable immediate action. We assume that each language model has a local module inside that is suitable for a specific function. First, this work identifies a set of modules showing consistent and local activation changes under an inference workload through activation-based analysis. Subsequently, we transplant an internal module that is properly activated for a specific task into the target model, leading to immediate and measurable functional changes without additional training or fine-tuning. To experimentally demonstrate the effectiveness of the transplant technique, we quantify the relationship between transplant strength and performance improvement under different conditions for two language models. In the cross-generation setting, we find that transplanting activation-selected modules can substantially improve the underperforming model, reaching up to twice the target baseline and achieving gap-based recovery above 100%. Moreover, in transplant experiments between a base model and its instruction-tuned counterpart, transplantation improves the underperforming model toward the stronger baseline, yielding up to about 2.33 times the target baseline with gap-based recovery reaching up to 100% in the best case. These results show that meaningful capacity transfer can be realized through the implantation of highly localized modules implied by language models. Overall, this work provides empirical evidence for task-localized modularity in language models and presents a new research area: model transplantation.


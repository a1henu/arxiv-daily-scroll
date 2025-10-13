---
layout: default
title: RO-Bench: Large-scale robustness evaluation of MLLMs with text-driven counterfactual videos
---

# RO-Bench: Large-scale robustness evaluation of MLLMs with text-driven counterfactual videos
**arXiv**：[2510.08936v1](https://arxiv.org/abs/2510.08936) · [PDF](https://arxiv.org/pdf/2510.08936.pdf)  
**作者**：Zixi Yang, Jiapeng Li, Muxi Diao, Yinuo Jing, Kongming Liang  
**一句话要点**：提出Ro-Bench基准以评估多模态大语言模型在反事实视频中的鲁棒性
**关键词**：多模态大语言模型, 视频理解, 鲁棒性评估, 反事实数据, 分布外测试, 基准构建

## 3 点简述
- 多模态大语言模型在视频理解任务中表现优异，但面对操纵视频内容时鲁棒性未知
- 通过编辑风格、对象、背景及其组合，构建动态分布外反事实视频测试集
- 评估显示模型性能显著下降，反事实数据微调可提升鲁棒性，在基准上性能提高21.73%

## 摘要（原文）

> Recently, Multi-modal Large Language Models (MLLMs) have demonstrated
> significant performance across various video understanding tasks. However,
> their robustness, particularly when faced with manipulated video content,
> remains largely unexplored. In this paper, we introduce Ro-Bench, the first
> benchmark for evaluating MLLMs on dynamic out-of-distribution (OOD)
> counterfactual video test sets. Ro-Bench incorporates high-quality, diverse and
> temporally relevant video data, by editing Style, Object, Background and their
> compositions. We evaluated eight recent video MLLMs and found that current
> models exhibit substantial performance degradation on Ro-Bench when exposed to
> counterfactual video content. Furthermore, we demonstrate that fine-tuning
> MLLMs with counterfactual data enhances robustness, achieving a 21.73%
> performance increase on Ro-Bench and a 12.78% improvement across 20 tasks in
> the MVBench dataset. These findings underscore the effectiveness of
> counterfactual data in enhancing the video understanding ability of MLLMs. The
> code and data will be released shortly.


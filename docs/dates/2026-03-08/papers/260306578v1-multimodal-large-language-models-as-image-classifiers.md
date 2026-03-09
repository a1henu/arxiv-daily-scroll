---
layout: default
title: Multimodal Large Language Models as Image Classifiers
---

# Multimodal Large Language Models as Image Classifiers
**arXiv**：[2603.06578v1](https://arxiv.org/abs/2603.06578) · [PDF](https://arxiv.org/pdf/2603.06578.pdf)  
**作者**：Nikita Kisel, Illia Volkov, Klara Janouskova, Jiri Matas  

**一句话要点**：揭示多模态大语言模型分类性能评估中的协议缺陷与标注噪声影响

**关键词**：多模态大语言模型, 图像分类评估, 标注噪声, 评估协议, 数据集重标注, 人工标注辅助

## 3 点简述
- 核心问题：MLLM分类性能评估存在协议不一致和标注噪声，导致与监督模型比较结论冲突。
- 方法要点：识别并修正评估协议关键问题，如输出映射、干扰项设计，并量化批次大小等设计选择影响。
- 实验或效果：使用ReGT重新标注数据集，MLLM性能提升达10.8%，缩小与监督模型差距，并展示辅助标注潜力。

## 摘要（原文）

> Multimodal Large Language Models (MLLM) classification performance depends critically on evaluation protocol and ground truth quality. Studies comparing MLLMs with supervised and vision-language models report conflicting conclusions, and we show these conflicts stem from protocols that either inflate or underestimate performance. Across the most common evaluation protocols, we identify and fix key issues: model outputs that fall outside the provided class list and are discarded, inflated results from weak multiple-choice distractors, and an open-world setting that underperforms only due to poor output mapping. We additionally quantify the impact of commonly overlooked design choices - batch size, image ordering, and text encoder selection - showing they substantially affect accuracy. Evaluating on ReGT, our multilabel reannotation of 625 ImageNet-1k classes, reveals that MLLMs benefit most from corrected labels (up to +10.8%), substantially narrowing the perceived gap with supervised models. Much of the reported MLLMs underperformance on classification is thus an artifact of noisy ground truth and flawed evaluation protocol rather than genuine model deficiency. Models less reliant on supervised training signals prove most sensitive to annotation quality. Finally, we show that MLLMs can assist human annotators: in a controlled case study, annotators confirmed or integrated MLLMs predictions in approximately 50% of difficult cases, demonstrating their potential for large-scale dataset curation.


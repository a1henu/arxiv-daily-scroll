---
layout: default
title: Representation Learning with Semantic-aware Instance and Sparse Token Alignments
---

# Representation Learning with Semantic-aware Instance and Sparse Token Alignments
**arXiv**：[2601.08165v1](https://arxiv.org/abs/2601.08165) · [PDF](https://arxiv.org/pdf/2601.08165.pdf)  
**作者**：Phuoc-Nguyen Bui, Toan Duc Nguyen, Junghyun Bum, Duc-Tai Le, Hyunseung Choo  

**一句话要点**：提出SISTA框架，通过语义感知实例与稀疏令牌对齐改进医学视觉-语言预训练。

**关键词**：医学视觉-语言预训练, 对比学习, 语义对齐, 多级对齐, 假负例消除, 细粒度任务

## 3 点简述
- 核心问题：医学数据中未配对样本可能语义相似，传统对比学习将其视为负例会破坏语义结构。
- 方法要点：在图像-报告和补丁-单词两个层级引入语义对齐，消除假负例并增强细粒度对应。
- 实验或效果：在图像分类、分割和检测任务上提升迁移性能，尤其在有限标注数据下表现显著。

## 摘要（原文）

> Medical contrastive vision-language pre-training (VLP) has demonstrated significant potential in improving performance on downstream tasks. Traditional approaches typically employ contrastive learning, treating paired image-report samples as positives and unpaired ones as negatives. However, in medical datasets, there can be substantial similarities between images or reports from different patients. Rigidly treating all unpaired samples as negatives, can disrupt the underlying semantic structure and negatively impact the quality of the learned representations. In this paper, we propose a multi-level alignment framework, Representation Learning with Semantic-aware Instance and Sparse Token Alignments (SISTA) by exploiting the semantic correspondence between medical image and radiology reports at two levels, i.e., image-report and patch-word levels. Specifically, we improve the conventional contrastive learning by incorporating inter-report similarity to eliminate the false negatives and introduce a method to effectively align image patches with relevant word tokens. Experimental results demonstrate the effectiveness of the proposed framework in improving transfer performance across different datasets on three downstream tasks: image classification, image segmentation, and object detection. Notably, our framework achieves significant improvements in fine-grained tasks even with limited labeled data. Codes and pre-trained models will be made available.


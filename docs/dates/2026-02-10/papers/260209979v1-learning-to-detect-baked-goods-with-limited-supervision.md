---
layout: default
title: Learning to Detect Baked Goods with Limited Supervision
---

# Learning to Detect Baked Goods with Limited Supervision
**arXiv**：[2602.09979v1](https://arxiv.org/abs/2602.09979) · [PDF](https://arxiv.org/pdf/2602.09979.pdf)  
**作者**：Thomas H. Schmitt, Maximilian Bundscherer, Tobias Bocklet  

**一句话要点**：提出弱监督与伪标签训练方法，以解决烘焙食品检测中标注数据稀缺的问题。

**关键词**：弱监督目标检测, 伪标签训练, 烘焙食品识别, 开放词汇检测器, YOLOv11

## 3 点简述
- 核心问题：德国烘焙食品种类多，全监督训练成本高，开放词汇检测器性能不足。
- 方法要点：结合OWLv2和Grounding DINO进行弱监督训练，利用Segment Anything 2生成伪标签提升鲁棒性。
- 实验或效果：仅图像级监督mAP达0.91，伪标签微调在非理想条件下提升19.3%，超越全监督基线。

## 摘要（原文）

> Monitoring leftover products provides valuable insights that can be used to optimize future production. This is especially important for German bakeries because freshly baked goods have a very short shelf life. Automating this process can reduce labor costs, improve accuracy, and streamline operations. We propose automating this process using an object detection model to identify baked goods from images. However, the large diversity of German baked goods makes fully supervised training prohibitively expensive and limits scalability. Although open-vocabulary detectors (e.g., OWLv2, Grounding DINO) offer lexibility, we demonstrate that they are insufficient for our task. While motivated by bakeries, our work addresses the broader challenges of deploying computer vision in industries, where tasks are specialized and annotated datasets are scarce. We compile dataset splits with varying supervision levels, covering 19 classes of baked goods. We propose two training workflows to train an object detection model with limited supervision. First, we combine OWLv2 and Grounding DINO localization with image-level supervision to train the model in a weakly supervised manner. Second, we improve viewpoint robustness by fine-tuning on video frames annotated using Segment Anything 2 as a pseudo-label propagation model. Using these workflows, we train YOLOv11 for our detection task due to its favorable speed accuracy tradeoff. Relying solely on image-level supervision, the model achieves a mean Average Precision (mAP) of 0.91. Finetuning with pseudo-labels raises model performance by 19.3% under non-ideal deployment conditions. Combining these workflows trains a model that surpasses our fully-supervised baseline model under non-ideal deployment conditions, despite relying only on image-level supervision.


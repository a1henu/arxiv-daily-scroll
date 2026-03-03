---
layout: default
title: GroupEnsemble: Efficient Uncertainty Estimation for DETR-based Object Detection
---

# GroupEnsemble: Efficient Uncertainty Estimation for DETR-based Object Detection
**arXiv**：[2603.01847v1](https://arxiv.org/abs/2603.01847) · [PDF](https://arxiv.org/pdf/2603.01847.pdf)  
**作者**：Yutong Yang, Katarina Popović, Julian Wiederer, Markus Braun, Vasileios Belagiannis, Bin Yang  

**一句话要点**：提出GroupEnsemble方法，以高效解决DETR类模型在目标检测中空间不确定性估计不足的问题。

**关键词**：目标检测, 不确定性估计, DETR模型, 深度学习, 自动驾驶

## 3 点简述
- DETR类模型仅能评估语义不确定性，缺乏空间不确定性，导致检测可靠性评估不完整。
- GroupEnsemble通过添加多样化查询组，在单次前向传播中并行预测多个检测集，实现高效不确定性估计。
- 在Cityscapes和COCO数据集上验证，结合MC-Dropout的混合方法以低成本超越Deep Ensembles性能。

## 摘要（原文）

> Detection Transformer (DETR) and its variants show strong performance on object detection, a key task for autonomous systems. However, a critical limitation of these models is that their confidence scores only reflect semantic uncertainty, failing to capture the equally important spatial uncertainty. This results in an incomplete assessment of the detection reliability. On the other hand, Deep Ensembles can tackle this by providing high-quality spatial uncertainty estimates. However, their immense memory consumption makes them impractical for real-world applications. A cheaper alternative, Monte Carlo (MC) Dropout, suffers from high latency due to the need of multiple forward passes during inference to estimate uncertainty.
>   To address these limitations, we introduce GroupEnsemble, an efficient and effective uncertainty estimation method for DETR-like models. GroupEnsemble simultaneously predicts multiple individual detection sets by feeding additional diverse groups of object queries to the transformer decoder during inference. Each query group is transformed by the shared decoder in isolation and predicts a complete detection set for the same input. An attention mask is applied to the decoder to prevent inter-group query interactions, ensuring each group detects independently to achieve reliable ensemble-based uncertainty estimation. By leveraging the decoder's inherent parallelism, GroupEnsemble efficiently estimates uncertainty in a single forward pass without sequential repetition. We validated our method under autonomous driving scenes and common daily scenes using the Cityscapes and COCO datasets, respectively. The results show that a hybrid approach combining MC-Dropout and GroupEnsemble outperforms Deep Ensembles on several metrics at a fraction of the cost. The code is available at https://github.com/yutongy98/GroupEnsemble.


---
layout: default
title: Self-Supervised Animal Identification for Long Videos
---

# Self-Supervised Animal Identification for Long Videos
**arXiv**：[2601.09663v1](https://arxiv.org/abs/2601.09663) · [PDF](https://arxiv.org/pdf/2601.09663.pdf)  
**作者**：Xuyang Fang, Sion Hannuna, Edwin Simpson, Neill Campbell  

**一句话要点**：提出高效自监督动物识别方法，将长视频个体识别重构为全局聚类任务，以解决内存限制和标注瓶颈。

**关键词**：自监督学习, 动物识别, 长视频分析, 全局聚类, 匈牙利算法, 资源受限计算

## 3 点简述
- 核心问题：长视频动物个体识别需大量手动标注，现有自监督方法因内存限制和时序误差传播不适用。
- 方法要点：假设视频中个体数量已知固定，基于边界框检测和总数，采样帧对并使用冻结预训练骨干，结合匈牙利算法自引导伪标签分配学习判别特征。
- 实验或效果：在3D-POP鸽子和8头小牛喂食数据集上，准确率超97%，GPU内存消耗低于1GB/批次，匹配或超越监督基线。

## 摘要（原文）

> Identifying individual animals in long-duration videos is essential for behavioral ecology, wildlife monitoring, and livestock management. Traditional methods require extensive manual annotation, while existing self-supervised approaches are computationally demanding and ill-suited for long sequences due to memory constraints and temporal error propagation. We introduce a highly efficient, self-supervised method that reframes animal identification as a global clustering task rather than a sequential tracking problem. Our approach assumes a known, fixed number of individuals within a single video -- a common scenario in practice -- and requires only bounding box detections and the total count. By sampling pairs of frames, using a frozen pre-trained backbone, and employing a self-bootstrapping mechanism with the Hungarian algorithm for in-batch pseudo-label assignment, our method learns discriminative features without identity labels. We adapt a Binary Cross Entropy loss from vision-language models, enabling state-of-the-art accuracy ($>$97\%) while consuming less than 1 GB of GPU memory per batch -- an order of magnitude less than standard contrastive methods. Evaluated on challenging real-world datasets (3D-POP pigeons and 8-calves feeding videos), our framework matches or surpasses supervised baselines trained on over 1,000 labeled frames, effectively removing the manual annotation bottleneck. This work enables practical, high-accuracy animal identification on consumer-grade hardware, with broad applicability in resource-constrained research settings. All code written for this paper are \href{https://huggingface.co/datasets/tonyFang04/8-calves}{here}.


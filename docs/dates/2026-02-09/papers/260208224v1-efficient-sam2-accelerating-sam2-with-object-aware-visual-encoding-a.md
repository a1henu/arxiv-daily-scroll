---
layout: default
title: Efficient-SAM2: Accelerating SAM2 with Object-Aware Visual Encoding and Memory Retrieval
---

# Efficient-SAM2: Accelerating SAM2 with Object-Aware Visual Encoding and Memory Retrieval
**arXiv**：[2602.08224v1](https://arxiv.org/abs/2602.08224) · [PDF](https://arxiv.org/pdf/2602.08224.pdf)  
**作者**：Jing Zhang, Zhikai Li, Xuewen Liu, Qingyi Gu  

**一句话要点**：提出Efficient-SAM2以加速SAM2在视频对象分割中的推理效率

**关键词**：视频对象分割, 推理加速, 稀疏计算, 注意力机制, 训练后优化

## 3 点简述
- 核心问题：SAM2在视频对象分割中计算负担重，影响实时处理，现有方法多关注轻量化骨干网络，缺乏训练后加速探索。
- 方法要点：基于SAM2的稀疏感知模式，设计对象感知的稀疏窗口路由和稀疏内存检索，消除背景区域和冗余内存计算。
- 实验或效果：在SAM2.1-L模型上实现1.68倍加速，SA-V测试集准确率仅下降1.0%，参数增加和训练开销可忽略。

## 摘要（原文）

> Segment Anything Model 2 (SAM2) shows excellent performance in video object segmentation tasks; however, the heavy computational burden hinders its application in real-time video processing. Although there have been efforts to improve the efficiency of SAM2, most of them focus on retraining a lightweight backbone, with little exploration into post-training acceleration. In this paper, we observe that SAM2 exhibits sparse perception pattern as biological vision, which provides opportunities for eliminating redundant computation and acceleration: i) In mask decoder, the attention primarily focuses on the foreground objects, whereas the image encoder in the earlier stage exhibits a broad attention span, which results in unnecessary computation to background regions. ii) In memory bank, only a small subset of tokens in each frame contribute significantly to memory attention, and the salient regions exhibit temporal consistency, making full-token computation redundant. With these insights, we propose Efficient-SAM2, which promotes SAM2 to adaptively focus on object regions while eliminating task-irrelevant computations, thereby significantly improving inference efficiency. Specifically, for image encoder, we propose object-aware Sparse Window Routing (SWR), a window-level computation allocation mechanism that leverages the consistency and saliency cues from the previous-frame decoder to route background regions into a lightweight shortcut branch. Moreover, for memory attention, we propose object-aware Sparse Memory Retrieval (SMR), which allows only the salient memory tokens in each frame to participate in computation, with the saliency pattern reused from their first recollection. With negligible additional parameters and minimal training overhead, Efficient-SAM2 delivers 1.68x speedup on SAM2.1-L model with only 1.0% accuracy drop on SA-V test set.


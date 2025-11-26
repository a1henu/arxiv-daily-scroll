---
layout: default
title: Short-Range Oversquashing
---

# Short-Range Oversquashing
**arXiv**：[2511.20406v1](https://arxiv.org/abs/2511.20406) · [PDF](https://arxiv.org/pdf/2511.20406.pdf)  
**作者**：Yaaqov Mishayev, Yonatan Sverdlov, Tal Amir, Nadav Dym  

**一句话要点**：揭示短程过压缩瓶颈现象，并比较MPNN与Transformer的解决能力

**关键词**：图神经网络, 过压缩现象, 短程瓶颈, Transformer模型, 消息传递网络, 梯度消失

## 3 点简述
- 核心问题：过压缩不仅限于长程任务，短程问题中也存在瓶颈现象和梯度消失。
- 方法要点：区分瓶颈现象与梯度消失机制，分析虚拟节点对短程过压缩的无效性。
- 实验或效果：Transformer在短程任务中表现优于MPNN，提供更优解决方案。

## 摘要（原文）

> Message Passing Neural Networks (MPNNs) are widely used for learning on graphs, but their ability to process long-range information is limited by the phenomenon of oversquashing. This limitation has led some researchers to advocate Graph Transformers as a better alternative, whereas others suggest that it can be mitigated within the MPNN framework, using virtual nodes or other rewiring techniques.
>   In this work, we demonstrate that oversquashing is not limited to long-range tasks, but can also arise in short-range problems. This observation allows us to disentangle two distinct mechanisms underlying oversquashing: (1) the bottleneck phenomenon, which can arise even in low-range settings, and (2) the vanishing gradient phenomenon, which is closely associated with long-range tasks.
>   We further show that the short-range bottleneck effect is not captured by existing explanations for oversquashing, and that adding virtual nodes does not resolve it. In contrast, transformers do succeed in such tasks, positioning them as the more compelling solution to oversquashing, compared to specialized MPNNs.


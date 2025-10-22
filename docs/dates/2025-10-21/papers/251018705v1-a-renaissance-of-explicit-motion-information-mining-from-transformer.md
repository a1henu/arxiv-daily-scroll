---
layout: default
title: A Renaissance of Explicit Motion Information Mining from Transformers for Action Recognition
---

# A Renaissance of Explicit Motion Information Mining from Transformers for Action Recognition
**arXiv**：[2510.18705v1](https://arxiv.org/abs/2510.18705) · [PDF](https://arxiv.org/pdf/2510.18705.pdf)  
**作者**：Peiqin Zhuang, Lei Bai, Yichao Wu, Ding Liang, Luping Zhou, Yali Wang, Wanli Ouyang  

**一句话要点**：提出EMIM模块，将成本体积运动建模融入Transformer以提升动作识别性能

**关键词**：动作识别, Transformer, 运动建模, 成本体积, 亲和矩阵, EMIM模块

## 3 点简述
- Transformer方法在动作识别中缺乏精细运动建模，导致在运动敏感数据集上表现不佳
- 通过构建成本体积式亲和矩阵，从下一帧采样关键令牌，同时建模外观和运动特征
- 在多个数据集上验证，尤其在Something-Something V1&V2上优于现有方法

## 摘要（原文）

> Recently, action recognition has been dominated by transformer-based methods,
> thanks to their spatiotemporal contextual aggregation capacities. However,
> despite the significant progress achieved on scene-related datasets, they do
> not perform well on motion-sensitive datasets due to the lack of elaborate
> motion modeling designs. Meanwhile, we observe that the widely-used cost volume
> in traditional action recognition is highly similar to the affinity matrix
> defined in self-attention, but equipped with powerful motion modeling
> capacities. In light of this, we propose to integrate those effective motion
> modeling properties into the existing transformer in a unified and neat way,
> with the proposal of the Explicit Motion Information Mining module (EMIM). In
> EMIM, we propose to construct the desirable affinity matrix in a cost volume
> style, where the set of key candidate tokens is sampled from the query-based
> neighboring area in the next frame in a sliding-window manner. Then, the
> constructed affinity matrix is used to aggregate contextual information for
> appearance modeling and is converted into motion features for motion modeling
> as well. We validate the motion modeling capacities of our method on four
> widely-used datasets, and our method performs better than existing
> state-of-the-art approaches, especially on motion-sensitive datasets, i.e.,
> Something-Something V1 & V2.


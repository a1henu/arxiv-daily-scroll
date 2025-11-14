---
layout: default
title: Explicit Temporal-Semantic Modeling for Dense Video Captioning via Context-Aware Cross-Modal Interaction
---

# Explicit Temporal-Semantic Modeling for Dense Video Captioning via Context-Aware Cross-Modal Interaction
**arXiv**：[2511.10134v1](https://arxiv.org/abs/2511.10134) · [PDF](https://arxiv.org/pdf/2511.10134.pdf)  
**作者**：Mingda Jia, Weiliang Meng, Zenghuang Fu, Yiheng Li, Qi Zeng, Yifan Zhang, Ju Xin, Rongtao Xu, Jiguang Zhang, Xiaopeng Zhang  

**一句话要点**：提出CACMI框架以解决密集视频描述中时间连贯性和语义完整性问题

**关键词**：密集视频描述, 时间语义建模, 跨模态交互, 上下文感知, 事件定位

## 3 点简述
- 密集视频描述方法依赖隐式建模，难以捕捉事件序列的时间连贯性和视觉上下文语义
- CACMI通过跨模态帧聚合和上下文感知特征增强，显式建模时间与语义
- 在ActivityNet Captions和YouCook2数据集上实现最先进性能

## 摘要（原文）

> Dense video captioning jointly localizes and captions salient events in untrimmed videos. Recent methods primarily focus on leveraging additional prior knowledge and advanced multi-task architectures to achieve competitive performance. However, these pipelines rely on implicit modeling that uses frame-level or fragmented video features, failing to capture the temporal coherence across event sequences and comprehensive semantics within visual contexts. To address this, we propose an explicit temporal-semantic modeling framework called Context-Aware Cross-Modal Interaction (CACMI), which leverages both latent temporal characteristics within videos and linguistic semantics from text corpus. Specifically, our model consists of two core components: Cross-modal Frame Aggregation aggregates relevant frames to extract temporally coherent, event-aligned textual features through cross-modal retrieval; and Context-aware Feature Enhancement utilizes query-guided attention to integrate visual dynamics with pseudo-event semantics. Extensive experiments on the ActivityNet Captions and YouCook2 datasets demonstrate that CACMI achieves the state-of-the-art performance on dense video captioning task.


---
layout: default
title: RelayGR: Scaling Long-Sequence Generative Recommendation via Cross-Stage Relay-Race Inference
---

# RelayGR: Scaling Long-Sequence Generative Recommendation via Cross-Stage Relay-Race Inference
**arXiv**：[2601.01712v1](https://arxiv.org/abs/2601.01712) · [PDF](https://arxiv.org/pdf/2601.01712.pdf)  
**作者**：Jiarui Wang, Huichao Chai, Yuanhang Zhang, Zongjin Zhou, Wei Guo, Xingkun Yang, Qiang Tang, Bo Pan, Jiawei Zhu, Ke Cheng, Yuting Yan, Shulan Wang, Yingjie Zhu, Zhengfan Yuan, Jiaqi Huang, Yuhan Zhang, Xiaosong Sun, Zhinan Zhang, Hong Zhu, Yongsheng Zhang, Tiantian Dong, Zhong Xiao, Deliang Liu, Chengzhou Lu, Yuan Sun, Zhiyuan Chen, Xinming Han, Zaizhu Liu, Yaoyuan Wang, Ziyang Zhang, Yong Liu, Jinxin Xu, Yajing Sun, Zhoujun Yu, Wenting Zhou, Qidong Zhang, Zhengyong Zhang, Zhonghai Gu, Yibo Jin, Yongxiang Feng, Pengfei Zuo  

**一句话要点**：提出RelayGR系统，通过跨阶段接力推理解决生成式推荐中长序列在线推理的延迟瓶颈。

**关键词**：生成式推荐, 长序列推理, 缓存优化, 实时系统, 延迟SLO, NPU部署

## 3 点简述
- 核心问题：实时推荐系统在严格尾延迟SLO下，生成式推荐模型因长序列推理时间受限，影响在线序列长度和推荐质量。
- 方法要点：采用选择性预推断用户行为前缀、亲和性路由确保缓存本地化、内存感知扩展器利用DRAM，实现HBM中接力推理以重用缓存。
- 实验或效果：在华为昇腾NPU上实现，固定P99 SLO下支持序列长度提升1.5倍，合规吞吐量提升达3.6倍。

## 摘要（原文）

> Real-time recommender systems execute multi-stage cascades (retrieval, pre-processing, fine-grained ranking) under strict tail-latency SLOs, leaving only tens of milliseconds for ranking. Generative recommendation (GR) models can improve quality by consuming long user-behavior sequences, but in production their online sequence length is tightly capped by the ranking-stage P99 budget. We observe that the majority of GR tokens encode user behaviors that are independent of the item candidates, suggesting an opportunity to pre-infer a user-behavior prefix once and reuse it during ranking rather than recomputing it on the critical path. Realizing this idea at industrial scale is non-trivial: the prefix cache must survive across multiple pipeline stages before the final ranking instance is determined, the user population implies cache footprints far beyond a single device, and indiscriminate pre-inference would overload shared resources under high QPS. We present RelayGR, a production system that enables in-HBM relay-race inference for GR. RelayGR selectively pre-infers long-term user prefixes, keeps their KV caches resident in HBM over the request lifecycle, and ensures the subsequent ranking can consume them without remote fetches. RelayGR combines three techniques: 1) a sequence-aware trigger that admits only at-risk requests under a bounded cache footprint and pre-inference load, 2) an affinity-aware router that co-locates cache production and consumption by routing both the auxiliary pre-infer signal and the ranking request to the same instance, and 3) a memory-aware expander that uses server-local DRAM to capture short-term cross-request reuse while avoiding redundant reloads. We implement RelayGR on Huawei Ascend NPUs and evaluate it with real queries. Under a fixed P99 SLO, RelayGR supports up to 1.5$\times$ longer sequences and improves SLO-compliant throughput by up to 3.6$\times$.


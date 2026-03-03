---
layout: default
title: IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
---

# IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
**arXiv**：[2603.01590v1](https://arxiv.org/abs/2603.01590) · [PDF](https://arxiv.org/pdf/2603.01590.pdf)  
**作者**：Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu  

**一句话要点**：提出IDProxy，利用多模态大语言模型生成代理嵌入，解决小红书广告与推荐中物品冷启动CTR预测问题。

**关键词**：冷启动CTR预测, 多模态大语言模型, 代理嵌入, 广告推荐系统, 端到端优化

## 3 点简述
- 核心问题：广告与推荐CTR模型依赖物品ID嵌入，在物品冷启动时因缺乏使用数据而效果不佳。
- 方法要点：利用多模态大语言模型从丰富内容信号生成代理嵌入，并与现有ID嵌入空间对齐，端到端优化CTR目标。
- 实验或效果：通过离线实验和在线A/B测试验证有效性，已部署于小红书探索流内容与展示广告，服务数亿用户。

## 摘要（原文）

> Click-through rate (CTR) models in advertising and recommendation systems rely heavily on item ID embeddings, which struggle in item cold-start settings. We present IDProxy, a solution that leverages multimodal large language models (MLLMs) to generate proxy embeddings from rich content signals, enabling effective CTR prediction for new items without usage data. These proxies are explicitly aligned with the existing ID embedding space and are optimized end-to-end under CTR objectives together with the ranking model, allowing seamless integration into existing large-scale ranking pipelines. Offline experiments and online A/B tests demonstrate the effectiveness of IDProxy, which has been successfully deployed in both Content Feed and Display Ads features of Xiaohongshu's Explore Feed, serving hundreds of millions of users daily.


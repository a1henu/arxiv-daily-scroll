---
layout: default
title: Referring Video Object Segmentation with Cross-Modality Proxy Queries
---

# Referring Video Object Segmentation with Cross-Modality Proxy Queries
**arXiv**：[2511.21139v1](https://arxiv.org/abs/2511.21139) · [PDF](https://arxiv.org/pdf/2511.21139.pdf)  
**作者**：Baoli Sun, Xinzhu Ma, Ning Wang, Zhihui Wang, Zhiyong Wang  

**一句话要点**：提出ProxyFormer以解决引用视频对象分割中的跨模态对齐与跟踪问题

**关键词**：引用视频对象分割, 跨模态对齐, 代理查询, Transformer结构, 语义一致性训练

## 3 点简述
- 核心问题：现有方法缺乏帧间依赖建模和文本约束延迟集成，导致目标跟踪不准确
- 方法要点：引入代理查询集成视觉与文本语义，通过多阶段更新增强跨模态对齐
- 实验或效果：在四个基准测试中优于现有方法，提升分割准确性和跟踪连贯性

## 摘要（原文）

> Referring video object segmentation (RVOS) is an emerging cross-modality task that aims to generate pixel-level maps of the target objects referred by given textual expressions. The main concept involves learning an accurate alignment of visual elements and language expressions within a semantic space. Recent approaches address cross-modality alignment through conditional queries, tracking the target object using a query-response based mechanism built upon transformer structure. However, they exhibit two limitations: (1) these conditional queries lack inter-frame dependency and variation modeling, making accurate target tracking challenging amid significant frame-to-frame variations; and (2) they integrate textual constraints belatedly, which may cause the video features potentially focus on the non-referred objects. Therefore, we propose a novel RVOS architecture called ProxyFormer, which introduces a set of proxy queries to integrate visual and text semantics and facilitate the flow of semantics between them. By progressively updating and propagating proxy queries across multiple stages of video feature encoder, ProxyFormer ensures that the video features are focused on the object of interest. This dynamic evolution also enables the establishment of inter-frame dependencies, enhancing the accuracy and coherence of object tracking. To mitigate high computational costs, we decouple cross-modality interactions into temporal and spatial dimensions. Additionally, we design a Joint Semantic Consistency (JSC) training strategy to align semantic consensus between the proxy queries and the combined video-text pairs. Comprehensive experiments on four widely used RVOS benchmarks demonstrate the superiority of our ProxyFormer to the state-of-the-art methods.


---
layout: default
title: E.M.Ground: A Temporal Grounding Vid-LLM with Holistic Event Perception and Matching
---

# E.M.Ground: A Temporal Grounding Vid-LLM with Holistic Event Perception and Matching
**arXiv**：[2602.05215v1](https://arxiv.org/abs/2602.05215) · [PDF](https://arxiv.org/pdf/2602.05215.pdf)  
**作者**：Jiahao Nie, Wenbin An, Gongjie Zhang, Yicheng Xu, Yap-Peng Tan, Alex C. Kot, Shijian Lu  

**一句话要点**：提出E.M.Ground以解决视频大语言模型在时序视频定位中的语义连续性问题

**关键词**：时序视频定位, 视频大语言模型, 事件感知, 语义连续性, 帧特征聚合, 噪声平滑

## 3 点简述
- 核心问题：现有方法依赖精确时间戳匹配起止帧，忽略事件语义连续性，导致定位模糊。
- 方法要点：引入<event>令牌聚合事件所有帧信息，使用Savitzky-Golay平滑减少噪声，多粒度帧特征聚合增强匹配可靠性。
- 实验或效果：在基准数据集上显著超越现有最先进视频大语言模型，验证了方法的有效性。

## 摘要（原文）

> Despite recent advances in Video Large Language Models (Vid-LLMs), Temporal Video Grounding (TVG), which aims to precisely localize time segments corresponding to query events, remains a significant challenge. Existing methods often match start and end frames by comparing frame features with two separate tokens, relying heavily on exact timestamps. However, this approach fails to capture the event's semantic continuity and integrity, leading to ambiguities. To address this, we propose E.M.Ground, a novel Vid-LLM for TVG that focuses on holistic and coherent event perception. E.M.Ground introduces three key innovations: (i) a special <event> token that aggregates information from all frames of a query event, preserving semantic continuity for accurate event matching; (ii) Savitzky-Golay smoothing to reduce noise in token-to-frame similarities across timestamps, improving prediction accuracy; (iii) multi-grained frame feature aggregation to enhance matching reliability and temporal understanding, compensating for compression-induced information loss. Extensive experiments on benchmark datasets show that E.M.Ground consistently outperforms state-of-the-art Vid-LLMs by significant margins.


---
layout: default
title: Puda: Private User Dataset Agent for User-Sovereign and Privacy-Preserving Personalized AI
---

# Puda: Private User Dataset Agent for User-Sovereign and Privacy-Preserving Personalized AI
**arXiv**：[2602.08268v1](https://arxiv.org/abs/2602.08268) · [PDF](https://arxiv.org/pdf/2602.08268.pdf)  
**作者**：Akinori Maeda, Yuto Sekiya, Sota Sugimura, Tomoya Asai, Yu Tsuda, Kohei Ikeda, Hiroshi Fujii, Kohei Watanabe  

**一句话要点**：提出Puda架构以解决用户数据主权与隐私保护在个性化AI中的平衡问题

**关键词**：用户数据主权, 隐私保护, 个性化AI, 浏览器代理, 多粒度管理, LLM评估

## 3 点简述
- 核心问题：平台数据孤岛限制用户主权，个性化AI需求与隐私保护存在冲突
- 方法要点：设计用户主权架构，聚合跨服务数据，支持客户端三级隐私粒度管理
- 实验或效果：在旅行规划任务中，预定义类别子集达到详细浏览历史97.2%的个性化性能

## 摘要（原文）

> Personal data centralization among dominant platform providers including search engines, social networking services, and e-commerce has created siloed ecosystems that restrict user sovereignty, thereby impeding data use across services. Meanwhile, the rapid proliferation of Large Language Model (LLM)-based agents has intensified demand for highly personalized services that require the dynamic provision of diverse personal data. This presents a significant challenge: balancing the utilization of such data with privacy protection. To address this challenge, we propose Puda (Private User Dataset Agent), a user-sovereign architecture that aggregates data across services and enables client-side management. Puda allows users to control data sharing at three privacy levels: (i) Detailed Browsing History, (ii) Extracted Keywords, and (iii) Predefined Category Subsets. We implemented Puda as a browser-based system that serves as a common platform across diverse services and evaluated it through a personalized travel planning task. Our results show that providing Predefined Category Subsets achieves 97.2% of the personalization performance (evaluated via an LLM-as-a-Judge framework across three criteria) obtained when sharing Detailed Browsing History. These findings demonstrate that Puda enables effective multi-granularity management, offering practical choices to mitigate the privacy-personalization trade-off. Overall, Puda provides an AI-native foundation for user sovereignty, empowering users to safely leverage the full potential of personalized AI.


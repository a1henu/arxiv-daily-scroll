---
layout: default
title: Confundo: Learning to Generate Robust Poison for Practical RAG Systems
---

# Confundo: Learning to Generate Robust Poison for Practical RAG Systems
**arXiv**：[2602.06616v1](https://arxiv.org/abs/2602.06616) · [PDF](https://arxiv.org/pdf/2602.06616.pdf)  
**作者**：Haoyang Hu, Zhejun Jiang, Yueming Lyu, Junyuan Zhang, Yi Liu, Ka-Ho Chow  

**一句话要点**：提出Confundo学习框架以生成针对实用RAG系统的鲁棒性毒化内容

**关键词**：检索增强生成, 毒化攻击, 鲁棒性学习, 大语言模型微调, 系统安全

## 3 点简述
- 核心问题：现有毒化攻击在实用RAG系统中因内容预处理和查询不匹配而效果严重下降
- 方法要点：通过微调大语言模型作为毒化生成器，实现高有效性、鲁棒性和隐蔽性
- 实验或效果：在多种数据集和RAG配置下大幅超越现有攻击，即使存在防御措施

## 摘要（原文）

> Retrieval-augmented generation (RAG) is increasingly deployed in real-world applications, where its reference-grounded design makes outputs appear trustworthy. This trust has spurred research on poisoning attacks that craft malicious content, inject it into knowledge sources, and manipulate RAG responses. However, when evaluated in practical RAG systems, existing attacks suffer from severely degraded effectiveness. This gap stems from two overlooked realities: (i) content is often processed before use, which can fragment the poison and weaken its effect, and (ii) users often do not issue the exact queries anticipated during attack design. These factors can lead practitioners to underestimate risks and develop a false sense of security. To better characterize the threat to practical systems, we present Confundo, a learning-to-poison framework that fine-tunes a large language model as a poison generator to achieve high effectiveness, robustness, and stealthiness. Confundo provides a unified framework supporting multiple attack objectives, demonstrated by manipulating factual correctness, inducing biased opinions, and triggering hallucinations. By addressing these overlooked challenges, Confundo consistently outperforms a wide range of purpose-built attacks across datasets and RAG configurations by large margins, even in the presence of defenses. Beyond exposing vulnerabilities, we also present a defensive use case that protects web content from unauthorized incorporation into RAG systems via scraping, with no impact on user experience.


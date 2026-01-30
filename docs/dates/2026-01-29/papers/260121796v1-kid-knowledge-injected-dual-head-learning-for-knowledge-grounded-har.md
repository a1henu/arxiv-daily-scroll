---
layout: default
title: KID: Knowledge-Injected Dual-Head Learning for Knowledge-Grounded Harmful Meme Detection
---

# KID: Knowledge-Injected Dual-Head Learning for Knowledge-Grounded Harmful Meme Detection
**arXiv**：[2601.21796v1](https://arxiv.org/abs/2601.21796) · [PDF](https://arxiv.org/pdf/2601.21796.pdf)  
**作者**：Yaocong Li, Leihan Zhang, Le Zhang, Qiang Yan  

**一句话要点**：提出KID框架，通过知识注入与双头学习解决有害网络梗图的检测问题。

**关键词**：有害梗图检测, 知识注入, 双头学习, 标签约束蒸馏, 多语言数据集, 推理链

## 3 点简述
- 核心问题：网络梗图的隐含有害内容依赖背景知识，现有方法难以有效理解。
- 方法要点：采用标签约束蒸馏分解推理链，结合双头架构联合优化生成与分类目标。
- 实验或效果：在五个多语言数据集上实现SOTA性能，提升2.1%–19.7%，验证知识注入与双头学习的有效性。

## 摘要（原文）

> Internet memes have become pervasive carriers of digital culture on social platforms. However, their heavy reliance on metaphors and sociocultural context also makes them subtle vehicles for harmful content, posing significant challenges for automated content moderation. Existing approaches primarily focus on intra-modal and inter-modal signal analysis, while the understanding of implicit toxicity often depends on background knowledge that is not explicitly present in the meme itself. To address this challenge, we propose KID, a Knowledge-Injected Dual-Head Learning framework for knowledge-grounded harmful meme detection. KID adopts a label-constrained distillation paradigm to decompose complex meme understanding into structured reasoning chains that explicitly link visual evidence, background knowledge, and classification labels. These chains guide the learning process by grounding external knowledge in meme-specific contexts. In addition, KID employs a dual-head architecture that jointly optimizes semantic generation and classification objectives, enabling aligned linguistic reasoning while maintaining stable decision boundaries. Extensive experiments on five multilingual datasets spanning English, Chinese, and low-resource Bengali demonstrate that KID achieves SOTA performance on both binary and multi-label harmful meme detection tasks, improving over previous best methods by 2.1%--19.7% across primary evaluation metrics. Ablation studies further confirm the effectiveness of knowledge injection and dual-head joint learning, highlighting their complementary contributions to robust and generalizable meme understanding. The code and data are available at https://github.com/PotatoDog1669/KID.


---
layout: default
title: LikeThis! Empowering App Users to Submit UI Improvement Suggestions Instead of Complaints
---

# LikeThis! Empowering App Users to Submit UI Improvement Suggestions Instead of Complaints
**arXiv**：[2603.04245v1](https://arxiv.org/abs/2603.04245) · [PDF](https://arxiv.org/pdf/2603.04245.pdf)  
**作者**：Jialiang Wei, Ali Ebrahimi Pourasad, Walid Maalej  

**一句话要点**：提出LikeThis!以基于用户评论和截图生成UI改进建议，提升移动应用反馈质量

**关键词**：用户反馈增强, UI设计改进, 生成式人工智能, 移动应用开发, 人机协作

## 3 点简述
- 核心问题：用户反馈常模糊或破坏性，影响移动应用迭代。
- 方法要点：结合GenAI，从评论和截图生成多个UI改进方案供用户选择。
- 实验或效果：模型评估显示GPT-Image-1表现最佳，用户研究证实反馈可理解性和可操作性提升。

## 摘要（原文）

> User feedback is crucial for the evolution of mobile apps. However, research suggests that users tend to submit uninformative, vague, or destructive feedback. Unlike recent AI4SE approaches that focus on generating code and other development artifacts, our work aims at empowering users to submit better and more constructive UI feedback with concrete suggestions on how to improve the app. We propose LikeThis!, a GenAI-based approach that takes a user comment with the corresponding screenshot to immediately generate multiple improvement alternatives, from which the user can easily choose their preferred option. To evaluate LikeThis!, we first conducted a model benchmarking study based on a public dataset of carefully critiqued UI designs. The results show that GPT-Image-1 significantly outperformed three other state-of-the-art image generation models in improving the designs to address UI issues while keeping the fidelity and without introducing new issues. An intermediate step in LikeThis! is to generate a solution specification before sketching the design as a key to achieving effective improvement. Second, we conducted a user study with 10 production apps, where 15 users used LikeThis! to submit their feedback on encountered issues. Later, the developers of the apps assessed the understandability and actionability of the feedback with and without generated improvements. The results show that our approach helps generate better feedback from both user and developer perspectives, paving the way for AI-assisted user-developer collaboration.


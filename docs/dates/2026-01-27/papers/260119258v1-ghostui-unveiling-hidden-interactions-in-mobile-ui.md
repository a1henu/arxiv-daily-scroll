---
layout: default
title: GhostUI: Unveiling Hidden Interactions in Mobile UI
---

# GhostUI: Unveiling Hidden Interactions in Mobile UI
**arXiv**：[2601.19258v1](https://arxiv.org/abs/2601.19258) · [PDF](https://arxiv.org/pdf/2601.19258.pdf)  
**作者**：Minkyu Kweon, Seokhyeon Park, Soohyun Lee, You Been Lee, Jeongmin Rhee, Jinwook Seo  

**一句话要点**：提出GhostUI数据集以解决移动应用中隐藏交互检测的挑战

**关键词**：隐藏交互检测, 移动用户界面, 视觉语言模型, 任务自动化, 数据集构建

## 3 点简述
- 核心问题：移动应用中的隐藏交互（如长按和滑动）缺乏视觉线索，用户和移动代理难以发现。
- 方法要点：GhostUI提供前后截图、简化视图层次、手势元数据和任务描述，帮助视觉语言模型识别隐藏交互。
- 实验或效果：微调于GhostUI的模型在预测隐藏交互和推断交互后状态方面优于基线模型。

## 摘要（原文）

> Modern mobile applications rely on hidden interactions--gestures without visual cues like long presses and swipes--to provide functionality without cluttering interfaces. While experienced users may discover these interactions through prior use or onboarding tutorials, their implicit nature makes them difficult for most users to uncover. Similarly, mobile agents--systems designed to automate tasks on mobile user interfaces, powered by vision language models (VLMs)--struggle to detect veiled interactions or determine actions for completing tasks. To address this challenge, we present GhostUI, a new dataset designed to enable the detection of hidden interactions in mobile applications. GhostUI provides before-and-after screenshots, simplified view hierarchies, gesture metadata, and task descriptions, allowing VLMs to better recognize concealed gestures and anticipate post-interaction states. Quantitative evaluations with VLMs show that models fine-tuned on GhostUI outperform baseline VLMs, particularly in predicting hidden interactions and inferring post-interaction screens, underscoring GhostUI's potential as a foundation for advancing mobile task automation.


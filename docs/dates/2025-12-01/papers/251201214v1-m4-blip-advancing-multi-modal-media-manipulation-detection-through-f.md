---
layout: default
title: M4-BLIP: Advancing Multi-Modal Media Manipulation Detection through Face-Enhanced Local Analysis
---

# M4-BLIP: Advancing Multi-Modal Media Manipulation Detection through Face-Enhanced Local Analysis
**arXiv**：[2512.01214v1](https://arxiv.org/abs/2512.01214) · [PDF](https://arxiv.org/pdf/2512.01214.pdf)  
**作者**：Hang Wu, Ke Sun, Jiayi Ji, Xiaoshuai Sun, Rongrong Ji  

**一句话要点**：提出M4-BLIP框架，通过增强局部面部分析提升多模态媒体篡改检测性能

**关键词**：多模态媒体篡改检测, 局部特征提取, 面部先验知识, 特征对齐融合, 大语言模型集成

## 3 点简述
- 核心问题：现有多模态媒体篡改检测方法常忽视局部信息，尤其是面部区域的篡改。
- 方法要点：基于BLIP-2提取局部特征，结合面部先验知识，通过对齐融合模块整合局部与全局特征。
- 实验或效果：实验验证框架有效性，优于现有方法，并集成大语言模型提升结果可解释性。

## 摘要（原文）

> In the contemporary digital landscape, multi-modal media manipulation has emerged as a significant societal threat, impacting the reliability and integrity of information dissemination. Current detection methodologies in this domain often overlook the crucial aspect of localized information, despite the fact that manipulations frequently occur in specific areas, particularly in facial regions. In response to this critical observation, we propose the M4-BLIP framework. This innovative framework utilizes the BLIP-2 model, renowned for its ability to extract local features, as the cornerstone for feature extraction. Complementing this, we incorporate local facial information as prior knowledge. A specially designed alignment and fusion module within M4-BLIP meticulously integrates these local and global features, creating a harmonious blend that enhances detection accuracy. Furthermore, our approach seamlessly integrates with Large Language Models (LLM), significantly improving the interpretability of the detection outcomes. Extensive quantitative and visualization experiments validate the effectiveness of our framework against the state-of-the-art competitors.


---
layout: default
title: How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors
---

# How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors
**arXiv**：[2601.21961v1](https://arxiv.org/abs/2601.21961) · [PDF](https://arxiv.org/pdf/2601.21961.pdf)  
**作者**：Kuai Yu, Naicheng Yu, Han Wang, Rui Yang, Huan Zhang  

**一句话要点**：提出VAF评估管道以量化网页视觉属性对网络代理决策的影响

**关键词**：网络代理, 视觉属性, 决策评估, 网页交互, 用户界面设计

## 3 点简述
- 研究网络代理在良性场景中对视觉属性的偏好，而非仅关注对抗攻击鲁棒性
- 设计VAF管道，通过变体生成、浏览交互和验证三阶段量化视觉属性影响
- 实验表明背景对比度、项目大小、位置和卡片清晰度对代理行为影响显著

## 摘要（原文）

> Web agents have demonstrated strong performance on a wide range of web-based tasks. However, existing research on the effect of environmental variation has mostly focused on robustness to adversarial attacks, with less attention to agents' preferences in benign scenarios. Although early studies have examined how textual attributes influence agent behavior, a systematic understanding of how visual attributes shape agent decision-making remains limited. To address this, we introduce VAF, a controlled evaluation pipeline for quantifying how webpage Visual Attribute Factors influence web-agent decision-making. Specifically, VAF consists of three stages: (i) variant generation, which ensures the variants share identical semantics as the original item while only differ in visual attributes; (ii) browsing interaction, where agents navigate the page via scrolling and clicking the interested item, mirroring how human users browse online; (iii) validating through both click action and reasoning from agents, which we use the Target Click Rate and Target Mention Rate to jointly evaluate the effect of visual attributes. By quantitatively measuring the decision-making difference between the original and variant, we identify which visual attributes influence agents' behavior most. Extensive experiments, across 8 variant families (48 variants total), 5 real-world websites (including shopping, travel, and news browsing), and 4 representative web agents, show that background color contrast, item size, position, and card clarity have a strong influence on agents' actions, whereas font styling, text color, and item image clarity exhibit minor effects.


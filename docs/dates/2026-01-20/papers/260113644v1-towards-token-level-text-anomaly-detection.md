---
layout: default
title: Towards Token-Level Text Anomaly Detection
---

# Towards Token-Level Text Anomaly Detection
**arXiv**：[2601.13644v1](https://arxiv.org/abs/2601.13644) · [PDF](https://arxiv.org/pdf/2601.13644.pdf)  
**作者**：Yang Cao, Bicheng Yu, Sikun Yang, Ming Liu, Yujiu Yang  

**一句话要点**：提出令牌级文本异常检测框架，实现细粒度异常定位，应用于垃圾邮件和假新闻检测。

**关键词**：令牌级异常检测, 文本异常定位, 多级检测框架, 基准数据集, 垃圾邮件检测, 假新闻检测

## 3 点简述
- 现有文本异常检测方法局限于文档级分析，无法定位具体异常部分。
- 引入令牌级异常检测，定义文档和令牌级异常，提出统一多级检测框架。
- 构建三个带令牌级标签的基准数据集，实验显示框架优于6个基线方法。

## 摘要（原文）

> Despite significant progress in text anomaly detection for web applications such as spam filtering and fake news detection, existing methods are fundamentally limited to document-level analysis, unable to identify which specific parts of a text are anomalous. We introduce token-level anomaly detection, a novel paradigm that enables fine-grained localization of anomalies within text. We formally define text anomalies at both document and token-levels, and propose a unified detection framework that operates across multiple levels. To facilitate research in this direction, we collect and annotate three benchmark datasets spanning spam, reviews and grammar errors with token-level labels. Experimental results demonstrate that our framework get better performance than other 6 baselines, opening new possibilities for precise anomaly localization in text. All the codes and data are publicly available on https://github.com/charles-cao/TokenCore.


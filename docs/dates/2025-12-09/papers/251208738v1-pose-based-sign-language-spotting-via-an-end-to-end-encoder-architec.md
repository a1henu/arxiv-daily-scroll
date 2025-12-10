---
layout: default
title: Pose-Based Sign Language Spotting via an End-to-End Encoder Architecture
---

# Pose-Based Sign Language Spotting via an End-to-End Encoder Architecture
**arXiv**：[2512.08738v1](https://arxiv.org/abs/2512.08738) · [PDF](https://arxiv.org/pdf/2512.08738.pdf)  
**作者**：Samuel Ebimobowei Johnny, Blessed Guda, Emmanuel Enejo Aaron, Assane Gueye  

**一句话要点**：提出基于姿态的端到端编码器架构，用于手语检索中的特定手势检测任务。

**关键词**：手语定位, 姿态关键点, 端到端模型, 编码器架构, 二分类, 手语检索

## 3 点简述
- 核心问题：解决连续手语序列中特定手势的检测与检索，定义为手语定位任务。
- 方法要点：直接利用姿态关键点，采用编码器架构进行二分类，避免中间文本匹配。
- 实验或效果：在WSLP 2025数据集上达到61.88%准确率和60.00% F1分数，验证了框架有效性。

## 摘要（原文）

> Automatic Sign Language Recognition (ASLR) has emerged as a vital field for bridging the gap between deaf and hearing communities. However, the problem of sign-to-sign retrieval or detecting a specific sign within a sequence of continuous signs remains largely unexplored. We define this novel task as Sign Language Spotting. In this paper, we present a first step toward sign language retrieval by addressing the challenge of detecting the presence or absence of a query sign video within a sentence-level gloss or sign video. Unlike conventional approaches that rely on intermediate gloss recognition or text-based matching, we propose an end-to-end model that directly operates on pose keypoints extracted from sign videos. Our architecture employs an encoder-only backbone with a binary classification head to determine whether the query sign appears within the target sequence. By focusing on pose representations instead of raw RGB frames, our method significantly reduces computational cost and mitigates visual noise. We evaluate our approach on the Word Presence Prediction dataset from the WSLP 2025 shared task, achieving 61.88\% accuracy and 60.00\% F1-score. These results demonstrate the effectiveness of our pose-based framework for Sign Language Spotting, establishing a strong foundation for future research in automatic sign language retrieval and verification. Code is available at https://github.com/EbimoJohnny/Pose-Based-Sign-Language-Spotting


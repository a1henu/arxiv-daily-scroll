---
layout: default
title: Memo2496: Expert-Annotated Dataset and Dual-View Adaptive Framework for Music Emotion Recognition
---

# Memo2496: Expert-Annotated Dataset and Dual-View Adaptive Framework for Music Emotion Recognition
**arXiv**：[2512.13998v1](https://arxiv.org/abs/2512.13998) · [PDF](https://arxiv.org/pdf/2512.13998.pdf)  
**作者**：Qilin Li, C. L. Philip Chen, TongZhang  

**一句话要点**：提出Memo2496数据集与DAMER框架以解决音乐情感识别中数据质量低和特征漂移问题

**关键词**：音乐情感识别, 数据集标注, 双流注意力, 渐进学习, 特征漂移缓解

## 3 点简述
- 核心问题：音乐情感识别面临高质量标注数据稀缺和跨音轨特征漂移的挑战。
- 方法要点：DAMER框架整合双流注意力融合、渐进置信标注和风格锚定记忆学习三个模块。
- 实验或效果：在多个数据集上验证DAMER的先进性能，提升唤醒维度准确率最高达3.43%。

## 摘要（原文）

> Music Emotion Recogniser (MER) research faces challenges due to limited high-quality annotated datasets and difficulties in addressing cross-track feature drift. This work presents two primary contributions to address these issues. Memo2496, a large-scale dataset, offers 2496 instrumental music tracks with continuous valence arousal labels, annotated by 30 certified music specialists. Annotation quality is ensured through calibration with extreme emotion exemplars and a consistency threshold of 0.25, measured by Euclidean distance in the valence arousal space. Furthermore, the Dual-view Adaptive Music Emotion Recogniser (DAMER) is introduced. DAMER integrates three synergistic modules: Dual Stream Attention Fusion (DSAF) facilitates token-level bidirectional interaction between Mel spectrograms and cochleagrams via cross attention mechanisms; Progressive Confidence Labelling (PCL) generates reliable pseudo labels employing curriculum-based temperature scheduling and consistency quantification using Jensen Shannon divergence; and Style Anchored Memory Learning (SAML) maintains a contrastive memory queue to mitigate cross-track feature drift. Extensive experiments on the Memo2496, 1000songs, and PMEmo datasets demonstrate DAMER's state-of-the-art performance, improving arousal dimension accuracy by 3.43%, 2.25%, and 0.17%, respectively. Ablation studies and visualisation analyses validate each module's contribution. Both the dataset and source code are publicly available.


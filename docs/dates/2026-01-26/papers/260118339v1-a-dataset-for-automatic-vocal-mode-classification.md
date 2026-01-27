---
layout: default
title: A Dataset for Automatic Vocal Mode Classification
---

# A Dataset for Automatic Vocal Mode Classification
**arXiv**：[2601.18339v1](https://arxiv.org/abs/2601.18339) · [PDF](https://arxiv.org/pdf/2601.18339.pdf)  
**作者**：Reemt Hinrichs, Sonja Stephan, Alexander Lange, Jörn Ostermann  

**一句话要点**：提出声乐模式数据集以支持自动分类，用于技术辅助歌唱教学。

**关键词**：声乐模式分类, 歌唱教学数据集, 音频数据增强, ResNet基线模型, 专家标注

## 3 点简述
- 核心问题：缺乏数据阻碍声乐模式自动分类，影响歌唱教学技术发展。
- 方法要点：录制四位歌手的持续元音样本，使用多麦克风自然增强，提供专家标注。
- 实验或效果：基于ResNet18的基线分类在5折交叉验证中达到81.3%平衡准确率。

## 摘要（原文）

> The Complete Vocal Technique (CVT) is a school of singing developed in the past decades by Cathrin Sadolin et al.. CVT groups the use of the voice into so called vocal modes, namely Neutral, Curbing, Overdrive and Edge. Knowledge of the desired vocal mode can be helpful for singing students. Automatic classification of vocal modes can thus be important for technology-assisted singing teaching. Previously, automatic classification of vocal modes has been attempted without major success, potentially due to a lack of data. Therefore, we recorded a novel vocal mode dataset consisting of sustained vowels recorded from four singers, three of which professional singers with more than five years of CVT-experience. The dataset covers the entire vocal range of the subjects, totaling 3,752 unique samples. By using four microphones, thereby offering a natural data augmentation, the dataset consists of more than 13,000 samples combined. An annotation was created using three CVT-experienced annotators, each providing an individual annotation. The merged annotation as well as the three individual annotations come with the published dataset. Additionally, we provide some baseline classification results. The best balanced accuracy across a 5-fold cross validation of 81.3\,\% was achieved with a ResNet18. The dataset can be downloaded under https://zenodo.org/records/14276415.


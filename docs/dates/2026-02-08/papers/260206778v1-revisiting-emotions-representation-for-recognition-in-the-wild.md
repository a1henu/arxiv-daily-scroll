---
layout: default
title: Revisiting Emotions Representation for Recognition in the Wild
---

# Revisiting Emotions Representation for Recognition in the Wild
**arXiv**：[2602.06778v1](https://arxiv.org/abs/2602.06778) · [PDF](https://arxiv.org/pdf/2602.06778.pdf)  
**作者**：Joao Baptista Cardia Neto, Claudio Ferrari, Stefano Berretti  

**一句话要点**：提出基于VAD空间概率分布的情感表示方法，以解决野外复杂情感识别问题。

**关键词**：情感识别, 概率分布学习, VAD空间, 数据集重标注, 复杂情感表示

## 3 点简述
- 核心问题：传统单标签分类无法表示自发复杂情感，需处理多情感混合与感知模糊性。
- 方法要点：利用VAD空间映射，自动重标注数据集，将情感描述为概率分布混合。
- 实验或效果：初步实验展示优势，提供新研究方向，数据标注已公开。

## 摘要（原文）

> Facial emotion recognition has been typically cast as a single-label classification problem of one out of six prototypical emotions. However, that is an oversimplification that is unsuitable for representing the multifaceted spectrum of spontaneous emotional states, which are most often the result of a combination of multiple emotions contributing at different intensities. Building on this, a promising direction that was explored recently is to cast emotion recognition as a distribution learning problem. Still, such approaches are limited in that research datasets are typically annotated with a single emotion class. In this paper, we contribute a novel approach to describe complex emotional states as probability distributions over a set of emotion classes. To do so, we propose a solution to automatically re-label existing datasets by exploiting the result of a study in which a large set of both basic and compound emotions is mapped to probability distributions in the Valence-Arousal-Dominance (VAD) space. In this way, given a face image annotated with VAD values, we can estimate the likelihood of it belonging to each of the distributions, so that emotional states can be described as a mixture of emotions, enriching their description, while also accounting for the ambiguous nature of their perception. In a preliminary set of experiments, we illustrate the advantages of this solution and a new possible direction of investigation. Data annotations are available at https://github.com/jbcnrlz/affectnet-b-annotation.


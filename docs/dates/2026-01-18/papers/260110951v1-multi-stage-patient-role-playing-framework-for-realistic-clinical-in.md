---
layout: default
title: Multi-Stage Patient Role-Playing Framework for Realistic Clinical Interactions
---

# Multi-Stage Patient Role-Playing Framework for Realistic Clinical Interactions
**arXiv**：[2601.10951v1](https://arxiv.org/abs/2601.10951) · [PDF](https://arxiv.org/pdf/2601.10951.pdf)  
**作者**：Shijie Jiang, Zefan Zhang, Kehua Zhu, Tian Bai, Ruihong Zhao  

**一句话要点**：提出多阶段患者角色扮演框架以提升临床交互模拟的真实性与个性化

**关键词**：临床交互模拟, 患者角色扮演, 大型语言模型评估, 数据集构建, 个性化响应生成

## 3 点简述
- 现有临床交互模拟依赖通用或LLM生成数据，真实性不足且多样性受限
- 构建首个中文患者模拟数据集，基于五维角色结构，并通过少样本生成增强数据平衡
- 提出无需训练的多阶段框架，分解交互为三阶段，显著提升模型模拟性能

## 摘要（原文）

> The simulation of realistic clinical interactions plays a pivotal role in advancing clinical Large Language Models (LLMs) and supporting medical diagnostic education. Existing approaches and benchmarks rely on generic or LLM-generated dialogue data, which limits the authenticity and diversity of doctor-patient interactions. In this work, we propose the first Chinese patient simulation dataset (Ch-PatientSim), constructed from realistic clinical interaction scenarios to comprehensively evaluate the performance of models in emulating patient behavior. Patients are simulated based on a five-dimensional persona structure. To address issues of the persona class imbalance, a portion of the dataset is augmented using few-shot generation, followed by manual verification. We evaluate various state-of-the-art LLMs and find that most produce overly formal responses that lack individual personality. To address this limitation, we propose a training-free Multi-Stage Patient Role-Playing (MSPRP) framework, which decomposes interactions into three stages to ensure both personalization and realism in model responses. Experimental results demonstrate that our approach significantly improves model performance across multiple dimensions of patient simulation.


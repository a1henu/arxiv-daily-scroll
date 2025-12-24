---
layout: default
title: Spatio-Temporal Graphs Beyond Grids: Benchmark for Maritime Anomaly Detection
---

# Spatio-Temporal Graphs Beyond Grids: Benchmark for Maritime Anomaly Detection
**arXiv**：[2512.20086v1](https://arxiv.org/abs/2512.20086) · [PDF](https://arxiv.org/pdf/2512.20086.pdf)  
**作者**：Jeehong Kim, Youngseok Hwang, Minchan Kim, Sungho Bae, Hyunwoo Park  

**一句话要点**：提出海事异常检测基准数据集，支持多粒度评估以解决非网格时空图构建挑战。

**关键词**：时空图神经网络, 海事异常检测, 非网格系统, 多粒度评估, 基准数据集

## 3 点简述
- 核心问题：海事交通缺乏固定节点，时空图构建困难，异常检测面临轨迹稀疏、不规则和多粒度挑战。
- 方法要点：基于OMTAD扩展，引入节点级、边级和图级异常评估，计划使用LLM代理生成语义异常。
- 实验或效果：提供基准促进可复现性，推动非网格时空系统异常检测方法发展。

## 摘要（原文）

> Spatio-temporal graph neural networks (ST-GNNs) have achieved notable success in structured domains such as road traffic and public transportation, where spatial entities can be naturally represented as fixed nodes. In contrast, many real-world systems including maritime traffic lack such fixed anchors, making the construction of spatio-temporal graphs a fundamental challenge. Anomaly detection in these non-grid environments is particularly difficult due to the absence of canonical reference points, the sparsity and irregularity of trajectories, and the fact that anomalies may manifest at multiple granularities. In this work, we introduce a novel benchmark dataset for anomaly detection in the maritime domain, extending the Open Maritime Traffic Analysis Dataset (OMTAD) into a benchmark tailored for graph-based anomaly detection. Our dataset enables systematic evaluation across three different granularities: node-level, edge-level, and graph-level anomalies. We plan to employ two specialized LLM-based agents: \emph{Trajectory Synthesizer} and \emph{Anomaly Injector} to construct richer interaction contexts and generate semantically meaningful anomalies. We expect this benchmark to promote reproducibility and to foster methodological advances in anomaly detection for non-grid spatio-temporal systems.


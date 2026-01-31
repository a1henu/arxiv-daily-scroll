---
layout: default
title: GeoRC: A Benchmark for Geolocation Reasoning Chains
---

# GeoRC: A Benchmark for Geolocation Reasoning Chains
**arXiv**：[2601.21278v1](https://arxiv.org/abs/2601.21278) · [PDF](https://arxiv.org/pdf/2601.21278.pdf)  
**作者**：Mohit Talreja, Joshua Diao, Jim Thannikary James, Radu Casapu, Tejas Santanam, Ethan Mendes, Alan Ritter, Wei Xu, James Hays  

**一句话要点**：提出GeoRC基准以评估视觉语言模型在地理定位推理链中的解释能力

**关键词**：地理定位推理, 视觉语言模型评估, 专家标注基准, 推理链幻觉, 细粒度视觉属性, GeoGuessr游戏

## 3 点简述
- 视觉语言模型在地理定位预测中准确率高，但解释推理链时易产生幻觉，缺乏可审计性。
- 通过专家标注构建包含800条真实推理链的基准，覆盖多种视觉属性如车牌形状和建筑风格。
- 评估发现闭源模型预测接近人类专家，但开源模型在推理链生成上表现差，揭示细粒度视觉属性提取的局限性。

## 摘要（原文）

> Vision Language Models (VLMs) are good at recognizing the global location of a photograph -- their geolocation prediction accuracy rivals the best human experts. But many VLMs are startlingly bad at explaining which image evidence led to their prediction, even when their location prediction is correct. The reasoning chains produced by VLMs frequently hallucinate scene attributes to support their location prediction (e.g. phantom writing, imagined infrastructure, misidentified flora). In this paper, we introduce the first benchmark for geolocation reasoning chains. We focus on the global location prediction task in the popular GeoGuessr game which draws from Google Street View spanning more than 100 countries. We collaborate with expert GeoGuessr players, including the reigning world champion, to produce 800 ground truth reasoning chains for 500 query scenes. These expert reasoning chains address hundreds of different discriminative visual attributes such as license plate shape, architecture, and soil properties to name just a few. We evaluate LLM-as-a-judge and VLM-as-a-judge strategies for scoring VLM-generated reasoning chains against our expert reasoning chains and find that Qwen 3 LLM-as-a-judge correlates best with human scoring. Our benchmark reveals that while large, closed-source VLMs such as Gemini and GPT 5 rival human experts at prediction locations, they still lag behind human experts when it comes to producing auditable reasoning chains. Open weights VLMs such as Llama and Qwen catastrophically fail on our benchmark -- they perform only slightly better than a baseline in which an LLM hallucinates a reasoning chain with oracle knowledge of the photo location but no visual information at all. We believe the gap between human experts and VLMs on this task points to VLM limitations at extracting fine-grained visual attributes from high resolution images.


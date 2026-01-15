---
layout: default
title: A.X K1 Technical Report
---

# A.X K1 Technical Report
**arXiv**：[2601.09200v1](https://arxiv.org/abs/2601.09200) · [PDF](https://arxiv.org/pdf/2601.09200.pdf)  
**作者**：Sung Jun Cheon, Jaekyung Cho, Seongho Choi, Hyunjun Eun, Seokhwan Jo, Jaehyun Jun, Minsoo Kang, Jin Kim, Jiwon Kim, Minsang Kim, Sungwan Kim, Seungsik Kim, Tae Yoon Kim, Youngrang Kim, Hyeongmun Lee, Sangyeol Lee, Sungeun Lee, Youngsoon Lee, Yujin Lee, Seongmin Ok, Chanyong Park, Hyewoong Park, Junyoung Park, Hyunho Yang, Subin Yi, Soohyun Bae, Dhammiko Arya, Yongseok Choi, Sangho Choi, Dongyeon Cho, Seungmo Cho, Gyoungeun Han, Yong-jin Han, Seokyoung Hong, Hyeon Hwang, Wonbeom Jang, Minjeong Ju, Wonjin Jung, Keummin Ka, Sungil Kang, Dongnam Kim, Joonghoon Kim, Jonghwi Kim, SaeRom Kim, Sangjin Kim, Seongwon Kim, Youngjin Kim, Seojin Lee, Sunwoo Lee, Taehoon Lee, Chanwoo Park, Sohee Park, Sooyeon Park, Yohan Ra, Sereimony Sek, Seungyeon Seo, Gun Song, Sanghoon Woo, Janghan Yoon, Sungbin Yoon  

**一句话要点**：提出A.X K1大语言模型，通过可控推理设计解决推理能力与推理效率的平衡问题

**关键词**：混合专家模型, 可控推理, 韩语语言模型, 大规模预训练, 推理效率优化

## 3 点简述
- 核心问题：如何在大语言模型中平衡推理能力与推理效率，以支持多样化实际部署场景
- 方法要点：采用5190亿参数MoE架构，提出Think-Fusion训练方法实现用户可控的思考模式切换
- 实验效果：在韩语基准测试中表现突出，整体性能与主流开源模型相当

## 摘要（原文）

> We introduce A.X K1, a 519B-parameter Mixture-of-Experts (MoE) language model trained from scratch. Our design leverages scaling laws to optimize training configurations and vocabulary size under fixed computational budgets. A.X K1 is pre-trained on a corpus of approximately 10T tokens, curated by a multi-stage data processing pipeline. Designed to bridge the gap between reasoning capability and inference efficiency, A.X K1 supports explicitly controllable reasoning to facilitate scalable deployment across diverse real-world scenarios. We propose a simple yet effective Think-Fusion training recipe, enabling user-controlled switching between thinking and non-thinking modes within a single unified model. Extensive evaluations demonstrate that A.X K1 achieves performance competitive with leading open-source models, while establishing a distinctive advantage in Korean-language benchmarks.


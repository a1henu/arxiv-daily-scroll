---
layout: default
title: FiMI: A Domain-Specific Language Model for Indian Finance Ecosystem
---

# FiMI: A Domain-Specific Language Model for Indian Finance Ecosystem
**arXiv**：[2602.05794v1](https://arxiv.org/abs/2602.05794) · [PDF](https://arxiv.org/pdf/2602.05794.pdf)  
**作者**：Aboli Kathar, Aman Kumar, Anusha Kamath, Araveeti Srujan, Ashish Sharma, Chandra Bhushan, Dilip Asbe, Divya Sorate, Duddu Prasanth Kumar, Evan Acharya, Harsh Sharma, Hrithik Kadam, Kanishk Singla, Keyur Doshi, Kiran Praveen, Kolisetty Krishna SK, Krishanu Adhikary, Lokesh MPT, Mayurdeep Sonowal, Nadeem Shaikh, Navya Prakash, Nimit Kothari, Nitin Kukreja, Prashant Devadiga, Rakesh Paul, Ratanjeet Pratap Chauhan, Raunak Kalani, Raviraj Joshi, Shamanth MH, Shantanu Pandey, Shubham Soni, Siddharth Dixit, Smriti Jopat, Sunil Patel, Suraj Singh, Suvradip Paul, Tulasi Pilla, Utkarsh Vaidya, Vineeth Nambiar, Vishal Kanvaty, Yatharth Dedhia  

**一句话要点**：提出FiMI领域专用语言模型，针对印度金融生态系统优化数字支付工作流。

**关键词**：金融语言模型, 多语言处理, 工具调用, 指令微调, 印度金融

## 3 点简述
- 核心问题：印度金融领域缺乏专用语言模型，需处理多语言和复杂工作流如交易争议。
- 方法要点：基于Mistral Small 24B架构，通过多阶段训练，包括金融数据预训练和指令微调。
- 实验或效果：FiMI Base在金融推理基准上提升20%，FiMI Instruct在工具调用上优于基准87%。

## 摘要（原文）

> We present FiMI (Finance Model for India), a domain-specialized financial language model developed for Indian digital payment systems. We develop two model variants: FiMI Base and FiMI Instruct. FiMI adapts the Mistral Small 24B architecture through a multi-stage training pipeline, beginning with continuous pre-training on 68 Billion tokens of curated financial, multilingual (English, Hindi, Hinglish), and synthetic data. This is followed by instruction fine-tuning and domain-specific supervised fine-tuning focused on multi-turn, tool-driven conversations that model real-world workflows, such as transaction disputes and mandate lifecycle management. Evaluations reveal that FiMI Base achieves a 20% improvement over the Mistral Small 24B Base model on finance reasoning benchmark, while FiMI Instruct outperforms the Mistral Small 24B Instruct model by 87% on domain-specific tool-calling. Moreover, FiMI achieves these significant domain gains while maintaining comparable performance to models of similar size on general benchmarks.


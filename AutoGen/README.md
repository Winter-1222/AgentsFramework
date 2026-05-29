# AutoGen 软件开发团队

基于 AutoGen 框架的多智能体协作开发系统，由产品经理、工程师、代码审查员和测试员组成团队，共同完成软件开发任务。

## 环境配置

1. 安装依赖：
```
pip install -r requirements.txt
```

2. 配置 `.env` 文件：
```
LLM_API_KEY=your_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_ID=qwen-max
```

## 运行

```bash
python autogen_software_team.py
```

团队协作流程：产品经理 → 工程师 → 代码审查员 → 测试员 → 自动终止。

## 比特币价格应用

`app.py` 是由 AI 团队生成的比特币价格展示应用，基于 Streamlit 构建。

```bash
streamlit run app.py
```

依赖：`requests`、`streamlit`

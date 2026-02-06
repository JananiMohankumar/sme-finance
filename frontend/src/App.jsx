import { useState } from "react";
import axios from "axios";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer
} from "recharts";

import "./App.css";

function App() {

  const [file, setFile] = useState(null);
  const [business, setBusiness] = useState("");
  const [industry, setIndustry] = useState("Retail");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please upload a file");
      return;
    }

    const form = new FormData();
    form.append("file", file);
    form.append("business_name", business);
    form.append("industry", industry);

    try {
      setLoading(true);
      setError("");

      const res = await axios.post(
        "https://sme-finance-backend-0u11.onrender.com/analyze",
        form
      );

      setResult(res.data);

    } catch (err) {
      setError("Failed to analyze file");
    } finally {
      setLoading(false);
    }
  };

  const metricChartData = result ? [
    { name: "Revenue", value: result.metrics.revenue },
    { name: "Expenses", value: result.metrics.expenses },
    { name: "Profit", value: result.metrics.profit }
  ] : [];

  return (
    <div className="page">

      <header className="header">
        <h1>SME Financial Health Platform</h1>
        <p>AI-powered financial analysis for small businesses</p>
      </header>

      <main className="container">

        {/* ---------------- How this platform works ---------------- */}

        <section className="features-section">

          <h2 className="section-title">How this platform works</h2>

          <div className="card-grid">

            <div className="feature-card fade-in">
              <h4>Upload your financial data</h4>
              <p>Upload CSV, Excel, Word or PDF files containing your revenue and expense transactions.</p>
            </div>

            <div className="feature-card fade-in delay1">
              <h4>Automatic financial analysis</h4>
              <p>Revenue, expenses, profit, profit margin and credit score are calculated automatically.</p>
            </div>

            <div className="feature-card fade-in delay2">
              <h4>AI powered reports</h4>
              <p>Easy to understand business reports are generated in English and Hindi.</p>
            </div>

            <div className="feature-card fade-in delay3">
              <h4>Forecasting and bookkeeping</h4>
              <p>Future revenue is predicted and expenses are automatically categorized.</p>
            </div>

          </div>
        </section>

        {/* ---------------- How to use ---------------- */}

        <section className="features-section">

          <h2 className="section-title">How to use</h2>

          <div className="steps-grid">

            <div className="step-card fade-in">
              <span>1</span>
              <p>Enter your business name</p>
            </div>

            <div className="step-card fade-in delay1">
              <span>2</span>
              <p>Select your industry</p>
            </div>

            <div className="step-card fade-in delay2">
              <span>3</span>
              <p>Upload your financial file</p>
            </div>

            <div className="step-card fade-in delay3">
              <span>4</span>
              <p>Click Analyze Business</p>
            </div>

            <div className="step-card fade-in delay4">
              <span>5</span>
              <p>View metrics, risks, forecast and reports</p>
            </div>

          </div>

        </section>

        {/* ---------------- What system provides ---------------- */}

        <section className="features-section">

          <h2 className="section-title">What this system provides</h2>

          <div className="card-grid">

            <div className="feature-card fade-in">
              Creditworthiness and financial health score
            </div>

            <div className="feature-card fade-in delay1">
              Risk identification
            </div>

            <div className="feature-card fade-in delay2">
              Revenue forecasting
            </div>

            <div className="feature-card fade-in delay3">
              Automated bookkeeping
            </div>

            <div className="feature-card fade-in delay4">
              Industry benchmarking
            </div>

            <div className="feature-card fade-in delay5">
              AI reports in English and Hindi
            </div>

            <div className="feature-card fade-in delay6">
              SME focused design for non-finance users
            </div>

          </div>

        </section>

        {/* ---------------- Upload ---------------- */}

        <div className="upload-section">
          <div className="card">

            <h2>Upload Financial Data</h2>

            <form onSubmit={handleSubmit} className="form">

              <div className="form-group">
                <label>Business Name</label>
                <input
                  type="text"
                  value={business}
                  onChange={e => setBusiness(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label>Industry</label>
                <select
                  value={industry}
                  onChange={e => setIndustry(e.target.value)}
                >
                  <option>Retail</option>
                  <option>Manufacturing</option>
                  <option>Services</option>
                  <option>Logistics</option>
                  <option>E-commerce</option>
                </select>
              </div>

              <div className="form-group">
                <label>Upload File</label>
                <input
                  type="file"
                  onChange={e => setFile(e.target.files[0])}
                />
              </div>

              {file && (
                <div className="file-info">
                  <span className="badge">
                    {file.name.split(".").pop().toUpperCase()}
                  </span>
                  <span className="file-name">{file.name}</span>
                </div>
              )}

              <button className="primary-btn" type="submit">
                Analyze Business
              </button>

            </form>

            {loading && <p className="info">Analyzing data…</p>}
            {error && <p className="error">{error}</p>}

          </div>
        </div>

        {/* ---------------- Results ---------------- */}

        {result && (
          <>

            {/* KPIs */}
            <div className="grid">

              <div className="stat">
                <h4>Credit Score</h4>
                <p>{result.credit_score}</p>
              </div>

              <div className="stat">
                <h4>Profit Margin</h4>
                <p>{result.metrics.profit_margin}%</p>
              </div>

              <div className="stat">
                <h4>Industry Performance</h4>
                <p>{result.benchmark.performance}</p>
              </div>

            </div>

            {/* -------- PDF download button -------- */}
            <div className="card">
              <h2>Investor Report</h2>

              <a
                className="primary-btn"
                style={{ textDecoration: "none", display: "inline-block" }}
                href={`http://127.0.0.1:8000/report/pdf/${result.id}`}
                target="_blank"
                rel="noreferrer"
              >
                Download Investor-ready PDF
              </a>
            </div>

            {/* -------- Chart -------- */}
            <div className="card">
              <h2>Financial Overview</h2>

              <div style={{ width: "100%", height: 320 }}>
                <ResponsiveContainer>
                  <BarChart data={metricChartData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="value" fill="#2563eb" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* -------- Risks -------- */}
            <div className="card">
              <h2>Risks</h2>
              {result.risks.length === 0
                ? <p>No major risks detected.</p>
                : (
                  <ul>
                    {result.risks.map((r, i) => <li key={i}>{r}</li>)}
                  </ul>
                )
              }
            </div>

            {/* -------- Forecast -------- */}
            <div className="card">
              <h2>Revenue Forecast</h2>

              {result.forecast.enabled ? (
                <table className="table">
                  <thead>
                    <tr>
                      <th>Month</th>
                      <th>Forecast Revenue</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.forecast.forecast.map((f, i) => (
                      <tr key={i}>
                        <td>{f.month}</td>
                        <td>{f.forecast_revenue}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              ) : (
                <p>{result.forecast.message}</p>
              )}
            </div>

            {/* -------- Bookkeeping -------- */}
            <div className="card">
              <h2>Automated Bookkeeping</h2>

              {result.bookkeeping.enabled ? (
                <ul>
                  {Object.entries(result.bookkeeping.category_summary).map(
                    ([k, v]) => <li key={k}>{k} : {v}</li>
                  )}
                </ul>
              ) : (
                <p>{result.bookkeeping.message}</p>
              )}
            </div>

            {/* -------- Recommended products -------- */}
            <div className="card">
              <h2>Recommended Financial Products</h2>

              {result.recommended_products &&
              result.recommended_products.length > 0 ? (
                <ul>
                  {result.recommended_products.map((p, i) => (
                    <li key={i}>{p}</li>
                  ))}
                </ul>
              ) : (
                <p>No recommendations available.</p>
              )}
            </div>

            {/* -------- Tax compliance -------- */}
            <div className="card">
              <h2>Tax & Compliance Check</h2>

              {result.tax_compliance?.enabled ? (
                result.tax_compliance.issues.length === 0 ? (
                  <p>No compliance issues detected.</p>
                ) : (
                  <ul>
                    {result.tax_compliance.issues.map((x, i) => (
                      <li key={i}>{x}</li>
                    ))}
                  </ul>
                )
              ) : (
                <p>{result.tax_compliance?.message}</p>
              )}
            </div>

            {/* -------- Reports -------- */}
            <div className="card">
              <h2>AI Report (English)</h2>
              <pre className="report">{result.report_en}</pre>
            </div>

            <div className="card">
              <h2>AI Report (Hindi)</h2>
              <pre className="report">{result.report_hi}</pre>
            </div>

          </>
        )}

      </main>

      <footer className="footer">
        © 2026 SME Financial Health Platform
      </footer>

    </div>
  );
}

export default App;
